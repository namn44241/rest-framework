# Copyright 2018 ACSONE SA/NV
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Base Rest",
    "summary": """
        Develop your own high level REST APIs for Odoo thanks to this addon.
        """,
    "version": "17.0.1.0.0",
    "development_status": "Beta",
    "license": "LGPL-3",
    "author": "ACSONE SA/NV, " "Odoo Community Association (OCA)",
    "maintainers": [],
    "website": "https://github.com/OCA/rest-framework",
    "depends": ["component", "web"],
    "data": [
        "views/web_assets.xml",
        "views/openapi_template.xml",
        "views/base_rest_view.xml",
    ],
    "assets": {
        "web.assets_common": [
            # Swagger UI library
            "/base_rest/static/lib/swagger-ui-3.51.1/swagger-ui-bundle.js",
            "/base_rest/static/lib/swagger-ui-3.51.1/swagger-ui-standalone-preset.js",
            "/base_rest/static/lib/swagger-ui-3.51.1/swagger-ui.css",
        ],
        "base_rest.assets_swagger": [
            "/base_rest/static/src/scss/base_rest.scss",
            "/base_rest/static/src/js/swagger_ui.js",
            "/base_rest/static/src/js/swagger.js",
        ],
    },
    "external_dependencies": {
        "python": [
            "cerberus",
            "pyquerystring",
            "parse-accept-language",
            # adding version causes missing-manifest-dependency false positives
            "apispec",
        ]
    },
    "installable": True,
    "application": True,
}
