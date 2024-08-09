from search.models import mark, model, part
import random

def create_parts(*, count: int) -> tuple[bool, str]:
    colors = ["красный", "синий", "белый", "черный", "зеленый", "оранжевый", "фиолетовый", "коричневый", "серый"]
    part_names = ["бампер", "фара", "капот", "крыло", "дверь", "подвеска", "руль", "салон", "багажник", "зеркало"]
    
    try:
        marks = mark.objects.all()
        models = model.objects.all()
    
        for _ in range(count):
            part_name = random.choice(part_names)
            random_mark = random.choice(marks)
            random_model = random.choice(models)
            price = random.randint(1000, 10000)
            json_data = {
                "color": random.choice(colors),
                "is_new_part": random.choice([True, False]),
                "count": random.randint(1, 10)
            }
        
            part.objects.create(
                name=part_name,
                mark=random_mark,
                model=random_model,
                price=price,
                json_data=json_data,
                is_visible=True
            )
            
            return True, ""
    except Exception as e:
        return False, str(e)