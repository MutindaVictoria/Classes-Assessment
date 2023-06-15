class Ancestralstories{
    constructor( story_name,length,moral_lesson,age_group){
        this.story_name = story_name
        this.length = length
        this.moral_lesson = moral_lesson
        this.age_group =age_group}}
   
        class Translator {
            constructor(name, languageFrom, languageTo) {
              this.name = name;
              this.languageFrom = languageFrom;
              this.languageTo = languageTo;
            }
          
            translate(story) {
              translate=[]
              translate.push(this.languageTo)
              return translate;
            }
          } 
