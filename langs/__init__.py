__all__ = ['lang']
from .languages import lang_en, lang_es, lang_pt
from .languages_sys import sudo_string_lang
languages  = {
  "en":    lang_en, "en-ar": lang_en, "en-arz": lang_en, "en-de":  lang_en, "en-es": lang_en,
  "en-fr": lang_en, "en-it": lang_en, "en-ja":  lang_en, "en-ko":  lang_en, "en-pt": lang_en,
  "ar":    lang_en, "ar-en": lang_en, "arz":    lang_en, "arz-en": lang_en,
  "es":    lang_es, "es-en": lang_en, "es-fr":  lang_en,
  "fr":    lang_en, "fr-en": lang_en, "fr-es":  lang_en,
  "it":    lang_en, "it-en": lang_en,
  "ja":    lang_en, "ja-en": lang_en,
  "ko":    lang_en, "ko-en": lang_en,
  "pt":    lang_pt, "pt-en": lang_en,
  "de":    lang_en, "de-en": lang_en,
}

def lang(text_, ln=None, sudo=None):
	ln = ln or  'en'
	if sudo != None:
		resp = sudo_string_lang[ln][0][text_]
	else:
		if ln in languages:
			ln = languages[ln]
		resp = ln[text_]
	return resp