# -*- coding: utf-8 -*-
if 0:
	from gluon import *
	request, session, response, T, cache = current.request, current.session, current.response, current.t, current.cache
	from gluon.dal import DAL
	from gluon.tools import Auth, Service, Crud, Storage
	db = DAL()
	auth = Auth()
	service = Service()
	crud = Crud()
	settings = Storage()

import uuid

db.define_table( 'plugin_mailcaptcha_queue',
							Field( 'uuid', 'string',
									label = T( 'UUID' ),
									requires = IS_NOT_EMPTY(),
									writable = False,
									default = lambda: str( uuid.uuid4() ),
									),
							Field( 'email', 'string',
									label = T( 'E-mail' ),
									requires = IS_NOT_EMPTY(),
									),
							auth.signature
 )
db.define_table( 'plugin_mailcaptcha_whitelist',
							Field( 'email', 'string',
									label = T( 'E-mail' ),
									requires = IS_NOT_EMPTY(),
									),
							auth.signature
 )
db.define_table( 'plugin_mailcaptcha_blacklist',
							Field( 'email', 'string',
									label = T( 'E-mail' ),
									requires = IS_NOT_EMPTY(),
									),
							auth.signature
 )
db.define_table( 'plugin_mailcaptcha_apply_on',
							Field( 'email', 'string',
									label = T( 'E-mail' ),
									requires = IS_NOT_EMPTY(),
									),
							auth.signature
 )
db.define_table( 'plugin_mailcaptcha_settings',
							Field( 'mail_from', 'string',
									label = T( 'Mail from' ),
									requires = IS_EMAIL(),
									),
							Field( 'mail_txt', 'text',
									label = T( 'Mail text' ),
									requires = IS_NOT_EMPTY(),
									comment = T( '%(url)s - URL, %(from)s - from email address, %(to) - to email address' ),
									),
							Field( 'recaptcha_private_key', 'string',
									label = T( 'Recaptcha private key' ),
									requires = IS_NOT_EMPTY(),
									),
							Field( 'recaptcha_public_key', 'string',
									label = T( 'Recaptcha public key' ),
									requires = IS_NOT_EMPTY(),
									),
							Field( 'recaptcha_options', 'string',
									label = T( 'Recaptcha options' ),
									),
							auth.signature
 )

plugin_mailcaptcha_config = db( db.plugin_mailcaptcha_settings.id > 0 ).select( orderby = db.plugin_mailcaptcha_settings.id ).first()

if auth.user:
	response.menu += [
								( T( 'Mailcaptcha' ), False, False,
									[
										( T( 'Whitelist' ), True, URL( 'plugin_mailcaptcha', 'whitelist' ), [] ),
										( T( 'Blacklist' ), True, URL( 'plugin_mailcaptcha', 'blacklist' ), [] ),
										( T( 'Apply on' ), True, URL( 'plugin_mailcaptcha', 'apply_on' ), [] ),
										( T( 'Settings' ), True, URL( 'plugin_mailcaptcha', 'settings' ), [] ),
										( T( 'Queue' ), True, URL( 'plugin_mailcaptcha', 'queue' ), [] ),
									] )
								]
