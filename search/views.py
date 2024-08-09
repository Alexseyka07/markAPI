from django.shortcuts import render, HttpResponse
from markAPI.parts_create import create_parts
from .filter import filter_mark_part_params, filter_marks_params, filter_other
from .models import mark, model, part
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def parts_create(request, count):
    result, error = create_parts()
    if result:
        return HttpResponse("Parts created")
    return HttpResponse(f"ERROR: {error}")


def models(request):
    list_models = model.objects.all()
    data = [{"name": m.name, "mark": m.mark.name } for m in list_models if m.is_visible]
    return JsonResponse(data, safe=False)

def marks(request):
    list_marks = list(mark.objects.all())
    data = [{"name": m.name, "producer_country_name": m.producer_country_name } for m in list_marks if m.is_visible]
    return JsonResponse(data, safe=False)


@csrf_exempt
def parts(request):
    query = json.loads(request.body)
    parts = part.objects.all()
    if "mark_name" in query and "part_name" in query and "params" in query:
        parts = filter_mark_part_params(query=query, parts=parts)
    elif "mark_list" in query and "part_name" in query and "params" in query:
        parts = filter_marks_params(query=query, parts=parts)
    else:
        parts = filter_other(query=query, parts=parts)
    
    min_price = 1000
    max_price = 10000
    if "price_gte" in query:
        min_price = query["price_gte"]
    if "price_lte" in query:
        max_price = query["price_lte"]
         
    response = []
    summ = 0
    for p in parts:
        if p.price > min_price and p.price < max_price: 
            res_p = {
                "mark": {
                    "id": p.mark.id,
                    "name": p.mark.name,
                    "producer_country_name": p.mark.producer_country_name
                },
                "model": {
                    "id": p.model.id,
                    "name": p.model.name
                },
                "name": p.name,
                "json_data": p.json_data,
                "price": p.price
            }
            summ += res_p["price"]
            response.append(res_p)
        
    page = int(query["page"])
    index = (page - 1) * 10
    response = response[index:(index+10)]
        
    result = {
        "response": response,
        "count": len(parts),
        "summ": summ
    }
        
    return JsonResponse(result, safe=False)