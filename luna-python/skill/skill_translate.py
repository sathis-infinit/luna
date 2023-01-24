def skill_translate(text,flang,tlang,needback=False):

    from translate import Translator
    translator= Translator(from_lang=flang,to_lang=tlang)
    translation = translator.translate(text)
    if needback:
        return translation
    else:
        print(translation)

# skill_translate("இப்போது நேரம் என்ன","tamil","english")

# வணக்கம்