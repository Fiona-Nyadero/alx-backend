0x02. i18n

Learning Objectives:
	- Learn how to parametrize Flask templates to display different languages
	- Learn how to infer the correct locale based on URL parameters, user settings or request headers
	- Learn how to localize timestamps
	- Extracting Text to Translate
	- Generating a Language Catalog
	- Using Translations
		gettext() and ngettext(), lazy_gettext()
	- Updating the Translations
	- Formatting Dates:
		 format_datetime(), format_date(), format_time() and format_timedelta()
		datetime.datetime (or datetime.date, datetime.time and datetime.timedelta), test_request_context()
	- Translating Dates and Times
	- Formatting Numbers:
		format_number(), format_decimal(), format_currency(), format_percent() and format_scientific()
		test_request_context()
	- Command-Line Enhancements
	- pytz
		Localized times and date arithmetic: localize(), astimezone(), normalize(), loc_dt, tzinfo, is_dst parameter to the utcoffset(), dst() && tzname() methods
		Problems with Localtime, Country Information, What is UTC, Helpers, Internationalization - i18n/l10n

Key Concepts:
	Flask-Babel, locale_selector(), timezoneselector(), refresh()
	Flask's request object accept_languages,  Accept-Language header
	gettext
	marking texts for translation with _(), get_locale()
	why the implemetation of this: flash(f'User {username} not found.') looks like this: flash(_('User %(username)s not found.', username=username))
	lazy evaluation version of _() i.e lazy_gettext()
	Why is this so: the {{ ... }} needs to be added, to force the _() to be evaluated instead of being considered a literal in the template

documentation documents each and every public class or function from Flask-Babel.
