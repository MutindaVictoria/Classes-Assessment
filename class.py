# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

# 1.input=oral story,different languages
#2.process= class Ancestral stories, attributes=length,moral lessons,age group,...
# methods=recording oral stories, translating different languages, create objects story,Storyteller,Translator
#3. output= recording oral stories,translating into different languages

class Ancestral stories:
    def__init__(self,story_name,length,moral_lesson,age_group):
        self.story_name = story_name
        self.length = length
        self.moral_lesson = moral_lesson
        self.age_group =age_group

class Story:
    def __init__(self, title, length, age_group, moral_lesson):
        self.title = title
        self.length = length
        self.age_group = age_group
        self.moral_lesson = moral_lesson

    def record_story(self):
        return f"recorded story is{title}"

    def translate_story(self, language):
        return f"{title} is translated in {language}"
class StoryTeller:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def tell_story(self, story):
        return f"tell story{self.title}for persons age{self.age}"
    def translate_story(self, story, language):
        return f"translate story {story} to{self.language}"
class Translator:
    def __init__(self, name, age, source_language, target_language):
        self.name = name
        self.age = age
        self.source_language = source_language
        self.target_language = target_language

    def translate_story(self, story):
        return f"translate {source_language}to {target_language}"
class Fable(Story):
    def __init__(self, title, length, age_group, moral_lesson, animal_characters):
        super().__init__(title, length, age_group, moral_lesson)
        self.animal_characters = animal_characters
class Elder(StoryTeller):
    def __init__(self, name, age, language, tribe):
        super().__init__(name, age, language)
        self.tribe = tribe

# # **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.


class Recipe:
    def __init__(self, name, ingredients, prep_time, cook_method, nutrition_info):
        self.name = name
        self.ingredients = ingredients
        self.prep_time = prep_time
        self.cook_method = cook_method
        self.nutrition_info = nutrition_info

    def display_recipe(self):
        print(f"Recipe Name: {self.name}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Preparation Time: {self.prep_time}")
        print(f"Cooking Method: {self.cook_method}")
        print(f"Nutritional Information: {self.nutrition_info}")

class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, prep_time, cook_method, nutrition_info, spiced_rice):
        super().__init__(name, ingredients, prep_time, cook_method, nutrition_info)
        self.spice_level = spice_level

    def display_recipe(self):
        super().display_recipe()
        print(f"Spice Level: {self.spiced_rice}")

class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, prep_time, cook_method, nutrition_info, njera_required):
        super().__init__(name, ingredients, prep_time, cook_method, nutrition_info)
        self.njera_required = njera_required

    def display_recipe(self):
        super().display_recipe()
        print(f"njera Required: {self.njera_required}")

class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, prep_time, cook_method, nutrition_info, oga_rice):
        super().__init__(name, ingredients, prep_time, cook_method, nutrition_info)
        self.oga_rice = oga_rice

    def display_recipe(self):
        super().display_recipe()
        print(f"Oga Rice: {self.oga_rice}")

# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

class Species:
    def __init__(self, name, diet, lifespan, habitat):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.habitat = habitat
    

class Prey(Species):
    def __init__(self, name, diet, lifespan, habitat, predators, migration_pattern):
        super().__init__(name, diet, lifespan, habitat)
        self.predators = predators
        self.migration_pattern = migration_pattern



class Predator(Species):
    def __init__(self, name, diet, lifespan, habitat, prey, hunting_style):
        super().__init__(name, diet, lifespan, habitat)
        self.prey = prey
        self.hunting_style = hunting_style

#   Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.  

# input = product 
#process= create class product, attributes(name,price,quantity),methods(calculate total value of product)


class Produc:
    def__init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity

    def total_value(self):
        returm self.price*self.quantity


# **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.

# input=Festival_lineup,artists,instruments,scheduling
#  process= scheduling performance,stage arrangements,coordinating performance
# output classes Artist,performance,stage,festival,attributes(artists,time,instruments,country,number of artists)
#   methods =add_performance,add_stage
class Artist:
    def__init__(self,name,country,instruments):
        self.name= name
        self.country
        self.instruments

class Performance:
    def__init__(self,artist,starting_time,finish_time):
        self.artist = artist
        self.starting_time = starting_time
        self. finish_time = finish_time

class Stage:
    def__init__(self,name,capacity):
        self.name= name
        self.capacity
        self.performances= []
    
    def add_performance(self,performance):
        self.performances.append(performance)


class Festival:
    def __init__(self):
        self.stages=[]
    
    def add_stage(self,stage):
        self.stages.append(stage)


    def add_performance(self,performance):
        for stage in self.stages:
            if len(stage.performance)==1:
                stage.add_performance(performance)
                return True
            elif performance.starting_time>=stage.performance[-2].finish_time:
                stage.add_performance(performance)
                return True
        return False

    

