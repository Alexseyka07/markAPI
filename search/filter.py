from .models import mark, model, part

def filter_mark_part_params(*,query, parts):
    parts = part.objects.filter(
            name = query["part_name"],
            mark__name=query["mark_name"],
            json_data__color = query["params"]["color"],
            is_visible=True,
        )
    
    return parts

def filter_marks_params(*,query, parts):
    parts = part.objects.filter(
            mark_id__in=[m for m in query["mark_list"]],
            json_data__is_new_part = query["params"]["is_new_part"],
            json_data__color = query["params"]["color"],
            is_visible=True,
        )
    
    return parts

def filter_other(*,query):
    parts = part.objects.all()
    if "model_name" in query:
            parts = parts.filter(
            model__name=query["model_name"])
    if "mark_name" in query:
            parts = parts.filter(
            mark__name=query["mark_name"])
    if "params" in query:
            parts = parts.filter(
            json_data__color = query["params"]["color"])
    if "is_visible" in query:
            parts = parts.filter(
            is_visible=query["is_visible"])
    if "part_name" in query:
            parts = parts.filter(
            name = query["part_name"])
            
    return parts