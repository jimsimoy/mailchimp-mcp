"""Mailchimp Marketing API operation table — GENERATED, do not edit by hand.

Every operation Mailchimp publishes, transcribed from its official OpenAPI
specification. Regenerate with::

    python tools/generate_operations.py

Source spec: https://api.mailchimp.com/schema/3.0/Swagger.json?expand
API reference: https://mailchimp.com/developer/marketing/api/
Spec version: 3.0.91
Generated: 298 operations (ADMIN: 74, BASIC: 75, READONLY: 149)

This module contains data only. `level` is the access level required to call the
operation: READONLY for GET, BASIC for POST, ADMIN for PUT/PATCH/DELETE.
"""

from __future__ import annotations

from typing import Any

SPEC_VERSION = "3.0.91"
SPEC_URL = "https://api.mailchimp.com/schema/3.0/Swagger.json?expand"

#: One entry per Mailchimp API operation. See module docstring for provenance.
OPERATIONS: list[dict[str, Any]] = [
    {
        "name": "get_root",
        "method": "GET",
        "path": "/",
        "level": "READONLY",
        "summary": "List api root resources",
        "description": "Get links to all other resources available in the API.",
        "group": "root",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_account_exports",
        "method": "GET",
        "path": "/account-exports",
        "level": "READONLY",
        "summary": "List account exports",
        "description": "Get a list of account exports for a given account.",
        "group": "account_exports",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_account_export",
        "method": "POST",
        "path": "/account-exports",
        "level": "BASIC",
        "summary": "Add export",
        "description": "Create a new account export in your Mailchimp account.",
        "group": "account_exports",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "include_stages"
        ],
        "body_description": "Creates an account export with the given parameters. Fields: include_stages, since_timestamp."
    },
    {
        "name": "get_account_export_id",
        "method": "GET",
        "path": "/account-exports/{export_id}",
        "level": "READONLY",
        "summary": "Get account export info",
        "description": "Get information about a specific account export.",
        "group": "account_export",
        "path_params": [
            {
                "name": "export_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the account export."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_activity_feed_chimp_chatter",
        "method": "GET",
        "path": "/activity-feed/chimp-chatter",
        "level": "READONLY",
        "summary": "Get latest chimp chatter",
        "description": "Return the Chimp Chatter for this account ordered by most recent.",
        "group": "activity_feed",
        "path_params": [],
        "query_params": [
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_audience_contacts",
        "method": "GET",
        "path": "/audiences",
        "level": "READONLY",
        "summary": "Get a list of audiences",
        "description": "Get information about all audiences in the account.",
        "group": "contacts",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_audience_id",
        "method": "GET",
        "path": "/audiences/{audience_id}",
        "level": "READONLY",
        "summary": "Get audience info",
        "description": "Get information about a specific audience.",
        "group": "contacts",
        "path_params": [
            {
                "name": "audience_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the audience."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_audience_contact_list",
        "method": "GET",
        "path": "/audiences/{audience_id}/contacts",
        "level": "READONLY",
        "summary": "Get Contacts",
        "description": "Get a list of omni-channel contacts for a given audience.",
        "group": "audiences",
        "path_params": [
            {
                "name": "audience_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the audience."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "cursor",
                "type": "str",
                "required": False,
                "description": "Paginate through a collection of records by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request. Default value fetches the first \"page\" of results."
            },
            {
                "name": "created_before",
                "type": "str",
                "required": False,
                "description": "Restricts the response to contacts created at or before the specified time (inclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00."
            },
            {
                "name": "created_since",
                "type": "str",
                "required": False,
                "description": "Restricts the response to contacts created after the specified time (exclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00."
            },
            {
                "name": "updated_before",
                "type": "str",
                "required": False,
                "description": "Restricts the response to contacts updated at or before the specified time (inclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00."
            },
            {
                "name": "updated_since",
                "type": "str",
                "required": False,
                "description": "Restricts the response to contacts updated after the specified time (exclusive). Uses ISO 8601 format: 2025-04-23T15:41:36+00:00."
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Specifies the field to sort the returned contacts by.",
                "enum": [
                    "created_at",
                    "updated_at"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "create_audience_contact",
        "method": "POST",
        "path": "/audiences/{audience_id}/contacts",
        "level": "BASIC",
        "summary": "Add Contact",
        "description": "Create a new omni-channel contact for an audience.",
        "group": "audiences",
        "path_params": [
            {
                "name": "audience_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the audience."
            }
        ],
        "query_params": [
            {
                "name": "merge_field_validation_mode",
                "type": "str",
                "required": False,
                "description": "Defines how merge field validation is handled. When set to `ignore_required_checks`, the API does not raise an error if required merge fields are missing from the request. When set to `strict`, the API enforces…",
                "enum": [
                    "ignore_required_checks",
                    "strict"
                ]
            },
            {
                "name": "data_mode",
                "type": "str",
                "required": False,
                "description": "Indicates the data processing mode. In `historical` mode, contact data changes do not trigger automations or webhooks. In `live mode`, such changes do trigger them.",
                "enum": [
                    "historical",
                    "live"
                ]
            }
        ],
        "has_body": True,
        "body_required": [],
        "body_description": "An instance of a contact. Fields: language, email_channel, sms_channel, merge_fields, tags, update_existing."
    },
    {
        "name": "get_audience_contact",
        "method": "GET",
        "path": "/audiences/{audience_id}/contacts/{contact_id}",
        "level": "READONLY",
        "summary": "Get Contact",
        "description": "Retrieve a specific omni-channel contact in an audience.",
        "group": "audiences",
        "path_params": [
            {
                "name": "audience_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the audience."
            },
            {
                "name": "contact_id",
                "type": "str",
                "required": True,
                "description": "A unique identifier for the contact, which can be a Mailchimp contact ID or a channel hash. A channel hash must follow the format email:[md5_hash] (where the hash is the MD5 of the lowercased email address) or…"
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_audience_contact",
        "method": "PATCH",
        "path": "/audiences/{audience_id}/contacts/{contact_id}",
        "level": "ADMIN",
        "summary": "Update Contact",
        "description": "Update an existing omni-channel contact.",
        "group": "audiences",
        "path_params": [
            {
                "name": "audience_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the audience."
            },
            {
                "name": "contact_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the contact."
            }
        ],
        "query_params": [
            {
                "name": "merge_field_validation_mode",
                "type": "str",
                "required": False,
                "description": "Defines how merge field validation is handled. When set to `ignore_required_checks`, the API does not raise an error if required merge fields are missing from the request. When set to `strict`, the API enforces…",
                "enum": [
                    "ignore_required_checks",
                    "strict"
                ]
            },
            {
                "name": "data_mode",
                "type": "str",
                "required": False,
                "description": "Indicates the data processing mode. In `historical` mode, contact data changes do not trigger automations or webhooks. In `live mode`, such changes do trigger them.",
                "enum": [
                    "historical",
                    "live"
                ]
            }
        ],
        "has_body": True,
        "body_required": [],
        "body_description": "An instance of a contact. Fields: language, email_channel, sms_channel, merge_fields, tags."
    },
    {
        "name": "post_audiences_contacts_actions_archive",
        "method": "POST",
        "path": "/audiences/{audience_id}/contacts/{contact_id}/actions/archive",
        "level": "BASIC",
        "summary": "Archive Contact",
        "description": "Archives a Contact.",
        "group": "contacts",
        "path_params": [
            {
                "name": "audience_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the audience."
            },
            {
                "name": "contact_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the contact."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_audiences_contacts_actions_forget",
        "method": "POST",
        "path": "/audiences/{audience_id}/contacts/{contact_id}/actions/forget",
        "level": "BASIC",
        "summary": "Forget Contact",
        "description": "Forgets a Contact.",
        "group": "contacts",
        "path_params": [
            {
                "name": "audience_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the audience."
            },
            {
                "name": "contact_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the contact."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_authorized_apps",
        "method": "GET",
        "path": "/authorized-apps",
        "level": "READONLY",
        "summary": "List authorized apps",
        "description": "Get a list of an account's registered, connected applications.",
        "group": "authorized_apps",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_authorized_apps_id",
        "method": "GET",
        "path": "/authorized-apps/{app_id}",
        "level": "READONLY",
        "summary": "Get authorized app info",
        "description": "Get information about a specific authorized application.",
        "group": "authorized_apps",
        "path_params": [
            {
                "name": "app_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the connected authorized application."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_automations",
        "method": "GET",
        "path": "/automations",
        "level": "READONLY",
        "summary": "List automations",
        "description": "Get a summary of an account's classic automations.",
        "group": "automations",
        "path_params": [],
        "query_params": [
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "before_create_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to automations created before this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_create_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to automations created after this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "before_start_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to automations started before this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_start_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to automations started after this time. Uses the ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "status",
                "type": "str",
                "required": False,
                "description": "Restrict the results to automations with the specified status.",
                "enum": [
                    "save",
                    "paused",
                    "sending"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_automations",
        "method": "POST",
        "path": "/automations",
        "level": "BASIC",
        "summary": "Add automation",
        "description": "Create a new classic automation in your Mailchimp account.",
        "group": "automations",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "recipients",
            "trigger_settings"
        ],
        "body_description": "A summary of an individual Automation workflow's settings and content. Fields: recipients, settings, trigger_settings."
    },
    {
        "name": "get_automations_id",
        "method": "GET",
        "path": "/automations/{workflow_id}",
        "level": "READONLY",
        "summary": "Get automation info",
        "description": "Get a summary of an individual classic automation workflow's settings and content. The `trigger_settings` object returns information for the first email in the workflow.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "archive_automations",
        "method": "POST",
        "path": "/automations/{workflow_id}/actions/archive",
        "level": "BASIC",
        "summary": "Archive automation",
        "description": "Archiving will permanently end your automation and keep the report data. You’ll be able to replicate your archived automation, but you can’t restart it.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_automations_id_actions_pause_all_emails",
        "method": "POST",
        "path": "/automations/{workflow_id}/actions/pause-all-emails",
        "level": "BASIC",
        "summary": "Pause automation emails",
        "description": "Pause all emails in a specific classic automation workflow.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_automations_id_actions_start_all_emails",
        "method": "POST",
        "path": "/automations/{workflow_id}/actions/start-all-emails",
        "level": "BASIC",
        "summary": "Start automation emails",
        "description": "Start all emails in a classic automation workflow.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_automations_id_emails",
        "method": "GET",
        "path": "/automations/{workflow_id}/emails",
        "level": "READONLY",
        "summary": "List automated emails",
        "description": "Get a summary of the emails in a classic automation workflow.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_automations_id_emails_id",
        "method": "GET",
        "path": "/automations/{workflow_id}/emails/{workflow_email_id}",
        "level": "READONLY",
        "summary": "Get workflow email info",
        "description": "Get information about an individual classic automation workflow email.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            },
            {
                "name": "workflow_email_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow email."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_automation_email_workflow_id",
        "method": "PATCH",
        "path": "/automations/{workflow_id}/emails/{workflow_email_id}",
        "level": "ADMIN",
        "summary": "Update workflow email",
        "description": "Update settings for a classic automation workflow email. Only works with workflows of type: abandonedBrowse, abandonedCart, emailFollowup, or singleWelcome.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            },
            {
                "name": "workflow_email_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow email."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Update information about an individual Automation workflow email. Fields: settings, delay."
    },
    {
        "name": "delete_automations_id_emails_id",
        "method": "DELETE",
        "path": "/automations/{workflow_id}/emails/{workflow_email_id}",
        "level": "ADMIN",
        "summary": "Delete workflow email",
        "description": "Removes an individual classic automation workflow email. Emails from certain workflow types, including the Abandoned Cart Email (abandonedCart) and Product Retargeting Email (abandonedBrowse) Workflows, cannot be deleted.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            },
            {
                "name": "workflow_email_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow email."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_automations_id_emails_id_actions_pause",
        "method": "POST",
        "path": "/automations/{workflow_id}/emails/{workflow_email_id}/actions/pause",
        "level": "BASIC",
        "summary": "Pause automated email",
        "description": "Pause an automated email.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            },
            {
                "name": "workflow_email_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow email."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_automations_id_emails_id_actions_start",
        "method": "POST",
        "path": "/automations/{workflow_id}/emails/{workflow_email_id}/actions/start",
        "level": "BASIC",
        "summary": "Start automated email",
        "description": "Start an automated email.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            },
            {
                "name": "workflow_email_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow email."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_automations_id_emails_id_queue",
        "method": "GET",
        "path": "/automations/{workflow_id}/emails/{workflow_email_id}/queue",
        "level": "READONLY",
        "summary": "List automated email subscribers",
        "description": "Get information about a classic automation email queue.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            },
            {
                "name": "workflow_email_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow email."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_automations_id_emails_id_queue",
        "method": "POST",
        "path": "/automations/{workflow_id}/emails/{workflow_email_id}/queue",
        "level": "BASIC",
        "summary": "Add subscriber to workflow email",
        "description": "Manually add a subscriber to a workflow, bypassing the default trigger settings. You can also use this endpoint to trigger a series of automated emails in an API 3.0 workflow type.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            },
            {
                "name": "workflow_email_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow email."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "email_address"
        ],
        "body_description": "Information about subscribers in an Automation email queue. Fields: email_address."
    },
    {
        "name": "get_automations_id_emails_id_queue_id",
        "method": "GET",
        "path": "/automations/{workflow_id}/emails/{workflow_email_id}/queue/{subscriber_hash}",
        "level": "READONLY",
        "summary": "Get automated email subscriber",
        "description": "Get information about a specific subscriber in a classic automation email queue.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            },
            {
                "name": "workflow_email_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow email."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_automations_id_removed_subscribers",
        "method": "GET",
        "path": "/automations/{workflow_id}/removed-subscribers",
        "level": "READONLY",
        "summary": "List subscribers removed from workflow",
        "description": "Get information about subscribers who were removed from a classic automation workflow.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_automations_id_removed_subscribers",
        "method": "POST",
        "path": "/automations/{workflow_id}/removed-subscribers",
        "level": "BASIC",
        "summary": "Remove subscriber from workflow",
        "description": "Remove a subscriber from a specific classic automation workflow. You can remove a subscriber at any point in an automation workflow, regardless of how many emails they've been sent from that workflow. Once they're removed, they can never be added back to the same workflow.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "email_address"
        ],
        "body_description": "Information about subscribers in an Automation email queue. Fields: email_address."
    },
    {
        "name": "get_automations_id_removed_subscribers_id",
        "method": "GET",
        "path": "/automations/{workflow_id}/removed-subscribers/{subscriber_hash}",
        "level": "READONLY",
        "summary": "Get subscriber removed from workflow",
        "description": "Get information about a specific subscriber who was removed from a classic automation workflow.",
        "group": "automations",
        "path_params": [
            {
                "name": "workflow_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the Automation workflow."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_batch_webhooks",
        "method": "GET",
        "path": "/batch-webhooks",
        "level": "READONLY",
        "summary": "List batch webhooks",
        "description": "Get all webhooks that have been configured for batches.",
        "group": "batch_webhooks",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_batch_webhooks",
        "method": "POST",
        "path": "/batch-webhooks",
        "level": "BASIC",
        "summary": "Add batch webhook",
        "description": "Configure a webhook that will fire whenever any batch request completes processing. You may only have a maximum of 20 batch webhooks.",
        "group": "batch_webhooks",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "url"
        ],
        "body_description": "Add a new Batch Webook. Fields: url, enabled."
    },
    {
        "name": "get_batch_webhook",
        "method": "GET",
        "path": "/batch-webhooks/{batch_webhook_id}",
        "level": "READONLY",
        "summary": "Get batch webhook info",
        "description": "Get information about a specific batch webhook.",
        "group": "batch_webhooks",
        "path_params": [
            {
                "name": "batch_webhook_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the batch webhook."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_batch_webhooks",
        "method": "PATCH",
        "path": "/batch-webhooks/{batch_webhook_id}",
        "level": "ADMIN",
        "summary": "Update batch webhook",
        "description": "Update a webhook that will fire whenever any batch request completes processing.",
        "group": "batch_webhooks",
        "path_params": [
            {
                "name": "batch_webhook_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the batch webhook."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Update an existing Batch Webook. Fields: url, enabled."
    },
    {
        "name": "delete_batch_webhook_id",
        "method": "DELETE",
        "path": "/batch-webhooks/{batch_webhook_id}",
        "level": "ADMIN",
        "summary": "Delete batch webhook",
        "description": "Remove a batch webhook. Webhooks will no longer be sent to the given URL.",
        "group": "batch_webhooks",
        "path_params": [
            {
                "name": "batch_webhook_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the batch webhook."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_batches",
        "method": "GET",
        "path": "/batches",
        "level": "READONLY",
        "summary": "List batch requests",
        "description": "Get a summary of batch requests that have been made.",
        "group": "batches",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_batches",
        "method": "POST",
        "path": "/batches",
        "level": "BASIC",
        "summary": "Start batch operation",
        "description": "Begin processing a batch operations request.",
        "group": "batches",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "operations"
        ],
        "body_description": "Fields: operations."
    },
    {
        "name": "get_batches_id",
        "method": "GET",
        "path": "/batches/{batch_id}",
        "level": "READONLY",
        "summary": "Get batch operation status",
        "description": "Get the status of a batch request.",
        "group": "batches",
        "path_params": [
            {
                "name": "batch_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the batch operation."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "delete_batches_id",
        "method": "DELETE",
        "path": "/batches/{batch_id}",
        "level": "ADMIN",
        "summary": "Delete batch request",
        "description": "Stops a batch request from running. Since only one batch request is run at a time, this can be used to cancel a long running request. The results of any completed operations will not be available after this call.",
        "group": "batches",
        "path_params": [
            {
                "name": "batch_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the batch operation."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_campaign_folders",
        "method": "GET",
        "path": "/campaign-folders",
        "level": "READONLY",
        "summary": "List campaign folders",
        "description": "Get all folders used to organize campaigns.",
        "group": "campaign_folders",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_campaign_folders",
        "method": "POST",
        "path": "/campaign-folders",
        "level": "BASIC",
        "summary": "Add campaign folder",
        "description": "Create a new campaign folder.",
        "group": "campaign_folders",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "A folder used to organize campaigns. Fields: name."
    },
    {
        "name": "get_campaign_folders_id",
        "method": "GET",
        "path": "/campaign-folders/{folder_id}",
        "level": "READONLY",
        "summary": "Get campaign folder",
        "description": "Get information about a specific folder used to organize campaigns.",
        "group": "campaign_folders",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign folder."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_campaign_folders_id",
        "method": "PATCH",
        "path": "/campaign-folders/{folder_id}",
        "level": "ADMIN",
        "summary": "Update campaign folder",
        "description": "Update a specific folder used to organize campaigns.",
        "group": "campaign_folders",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign folder."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "A folder used to organize campaigns. Fields: name."
    },
    {
        "name": "delete_campaign_folders_id",
        "method": "DELETE",
        "path": "/campaign-folders/{folder_id}",
        "level": "ADMIN",
        "summary": "Delete campaign folder",
        "description": "Delete a specific campaign folder, and mark all the campaigns in the folder as 'unfiled'.",
        "group": "campaign_folders",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign folder."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_campaigns",
        "method": "GET",
        "path": "/campaigns",
        "level": "READONLY",
        "summary": "List campaigns",
        "description": "Get all campaigns in an account.",
        "group": "campaigns",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "type",
                "type": "str",
                "required": False,
                "description": "The campaign type.",
                "enum": [
                    "regular",
                    "plaintext",
                    "absplit",
                    "rss",
                    "variate"
                ]
            },
            {
                "name": "status",
                "type": "str",
                "required": False,
                "description": "The status of the campaign.",
                "enum": [
                    "save",
                    "paused",
                    "schedule",
                    "sending",
                    "sent"
                ]
            },
            {
                "name": "before_send_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to campaigns sent before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_send_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to campaigns sent after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "before_create_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to campaigns created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_create_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to campaigns created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "list_id",
                "type": "str",
                "required": False,
                "description": "The unique id for the list."
            },
            {
                "name": "folder_id",
                "type": "str",
                "required": False,
                "description": "The unique folder id."
            },
            {
                "name": "member_id",
                "type": "str",
                "required": False,
                "description": "Retrieve campaigns sent to a particular list member. Member ID is The MD5 hash of the lowercase version of the list member’s email address."
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "create_time",
                    "send_time"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            },
            {
                "name": "include_resend_shortcut_eligibility",
                "type": "bool",
                "required": False,
                "description": "Return the `resend_shortcut_eligibility` field in the response, which tells you if the campaign is eligible for the various Campaign Resend Shortcuts offered."
            },
            {
                "name": "include_resend_shortcut_usage",
                "type": "bool",
                "required": False,
                "description": "Return the `resend_shortcut_usage` field in the response. This includes information about campaigns related by a shortcut."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_campaigns",
        "method": "POST",
        "path": "/campaigns",
        "level": "BASIC",
        "summary": "Add campaign",
        "description": "Create a new Mailchimp campaign.",
        "group": "campaigns",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "type"
        ],
        "body_description": "A summary of an individual campaign's settings and content. Fields: type, recipients, settings, variate_settings, tracking, rss_opts, social_card, content_type."
    },
    {
        "name": "get_campaigns_id",
        "method": "GET",
        "path": "/campaigns/{campaign_id}",
        "level": "READONLY",
        "summary": "Get campaign info",
        "description": "Get information about a specific campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "include_resend_shortcut_eligibility",
                "type": "bool",
                "required": False,
                "description": "Return the `resend_shortcut_eligibility` field in the response, which tells you if the campaign is eligible for the various Campaign Resend Shortcuts offered."
            },
            {
                "name": "include_resend_shortcut_usage",
                "type": "bool",
                "required": False,
                "description": "Return the `resend_shortcut_usage` field in the response. This includes information about campaigns related by a shortcut."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_campaigns_id",
        "method": "PATCH",
        "path": "/campaigns/{campaign_id}",
        "level": "ADMIN",
        "summary": "Update campaign settings",
        "description": "Update some or all of the settings for a specific campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "settings"
        ],
        "body_description": "A summary of an individual campaign's settings and content. Fields: recipients, settings, variate_settings, tracking, rss_opts, social_card."
    },
    {
        "name": "delete_campaigns_id",
        "method": "DELETE",
        "path": "/campaigns/{campaign_id}",
        "level": "ADMIN",
        "summary": "Delete campaign",
        "description": "Remove a campaign from your Mailchimp account.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_campaigns_id_actions_cancel_send",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/actions/cancel-send",
        "level": "BASIC",
        "summary": "Cancel campaign",
        "description": "Cancel a Regular or Plain-Text Campaign after you send, before all of your recipients receive it. This feature is included with Mailchimp Pro.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_campaigns_id_actions_create_resend",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/actions/create-resend",
        "level": "BASIC",
        "summary": "Resend campaign",
        "description": "Remove the guesswork for resending a campaign to certain segments. You can use this endpoint as a shortcut to replicate a campaign and resend it to common segments, such as those who didn't open the campaign, or any new subscribers since it was sent.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Fields: shortcut_type."
    },
    {
        "name": "post_campaigns_id_actions_pause",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/actions/pause",
        "level": "BASIC",
        "summary": "Pause rss campaign",
        "description": "Pause an RSS-Driven campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_campaigns_id_actions_replicate",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/actions/replicate",
        "level": "BASIC",
        "summary": "Replicate campaign",
        "description": "Replicate a campaign in saved or send status.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_campaigns_id_actions_resume",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/actions/resume",
        "level": "BASIC",
        "summary": "Resume rss campaign",
        "description": "Resume an RSS-Driven campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_campaigns_id_actions_schedule",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/actions/schedule",
        "level": "BASIC",
        "summary": "Schedule campaign",
        "description": "Schedule a campaign for delivery. If you're using Multivariate Campaigns to test send times or sending RSS Campaigns, use the send action instead.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "schedule_time"
        ],
        "body_description": "Fields: schedule_time, timewarp, batch_delivery."
    },
    {
        "name": "post_campaigns_id_actions_send",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/actions/send",
        "level": "BASIC",
        "summary": "Send campaign",
        "description": "Send a Mailchimp campaign. For RSS Campaigns, the campaign will send according to its schedule. All other campaigns will send immediately.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_campaigns_id_actions_test",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/actions/test",
        "level": "BASIC",
        "summary": "Send test email",
        "description": "Send a test email.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "test_emails",
            "send_type"
        ],
        "body_description": "Fields: test_emails, send_type."
    },
    {
        "name": "post_campaigns_id_actions_unschedule",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/actions/unschedule",
        "level": "BASIC",
        "summary": "Unschedule campaign",
        "description": "Unschedule a scheduled campaign that hasn't started sending.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_campaigns_id_content",
        "method": "GET",
        "path": "/campaigns/{campaign_id}/content",
        "level": "READONLY",
        "summary": "Get campaign content",
        "description": "Get the the HTML and plain-text content for a campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "put_campaigns_id_content",
        "method": "PUT",
        "path": "/campaigns/{campaign_id}/content",
        "level": "ADMIN",
        "summary": "Set campaign content",
        "description": "Set the content for a campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "The HTML and plain-text content for a campaign Fields: plain_text, html, url, template, archive, variate_contents."
    },
    {
        "name": "get_campaigns_id_feedback",
        "method": "GET",
        "path": "/campaigns/{campaign_id}/feedback",
        "level": "READONLY",
        "summary": "List campaign feedback",
        "description": "Get team feedback while you're working together on a Mailchimp campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_campaigns_id_feedback",
        "method": "POST",
        "path": "/campaigns/{campaign_id}/feedback",
        "level": "BASIC",
        "summary": "Add campaign feedback",
        "description": "Add feedback on a specific campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "message"
        ],
        "body_description": "A specific feedback message from a specific campaign. Fields: block_id, message, is_complete."
    },
    {
        "name": "get_campaigns_id_feedback_id",
        "method": "GET",
        "path": "/campaigns/{campaign_id}/feedback/{feedback_id}",
        "level": "READONLY",
        "summary": "Get campaign feedback message",
        "description": "Get a specific feedback message from a campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "feedback_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the feedback message."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_campaigns_id_feedback_id",
        "method": "PATCH",
        "path": "/campaigns/{campaign_id}/feedback/{feedback_id}",
        "level": "ADMIN",
        "summary": "Update campaign feedback message",
        "description": "Update a specific feedback message for a campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "feedback_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the feedback message."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "A specific feedback message from a specific campaign. Fields: block_id, message, is_complete."
    },
    {
        "name": "delete_campaigns_id_feedback_id",
        "method": "DELETE",
        "path": "/campaigns/{campaign_id}/feedback/{feedback_id}",
        "level": "ADMIN",
        "summary": "Delete campaign feedback message",
        "description": "Remove a specific feedback message for a campaign.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "feedback_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the feedback message."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_campaigns_id_send_checklist",
        "method": "GET",
        "path": "/campaigns/{campaign_id}/send-checklist",
        "level": "READONLY",
        "summary": "Get campaign send checklist",
        "description": "Review the send checklist for a campaign, and resolve any issues before sending.",
        "group": "campaigns",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_connected_sites",
        "method": "GET",
        "path": "/connected-sites",
        "level": "READONLY",
        "summary": "List connected sites",
        "description": "Get all connected sites in an account.",
        "group": "connected_sites",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_connected_sites",
        "method": "POST",
        "path": "/connected-sites",
        "level": "BASIC",
        "summary": "Add connected site",
        "description": "Create a new Mailchimp connected site.",
        "group": "connected_sites",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "foreign_id",
            "domain"
        ],
        "body_description": "Information about a specific connected site. Fields: foreign_id, domain."
    },
    {
        "name": "get_connected_sites_id",
        "method": "GET",
        "path": "/connected-sites/{connected_site_id}",
        "level": "READONLY",
        "summary": "Get connected site",
        "description": "Get information about a specific connected site.",
        "group": "connected_sites",
        "path_params": [
            {
                "name": "connected_site_id",
                "type": "str",
                "required": True,
                "description": "The unique identifier for the site."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "delete_connected_sites_id",
        "method": "DELETE",
        "path": "/connected-sites/{connected_site_id}",
        "level": "ADMIN",
        "summary": "Delete connected site",
        "description": "Remove a connected site from your Mailchimp account.",
        "group": "connected_sites",
        "path_params": [
            {
                "name": "connected_site_id",
                "type": "str",
                "required": True,
                "description": "The unique identifier for the site."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_connected_sites_id_actions_disable_pixel",
        "method": "POST",
        "path": "/connected-sites/{connected_site_id}/actions/disable-pixel",
        "level": "BASIC",
        "summary": "Disable pixel for connected site",
        "description": "Disable the Mailchimp tracking pixel for a connected site.",
        "group": "connected_sites",
        "path_params": [
            {
                "name": "connected_site_id",
                "type": "str",
                "required": True,
                "description": "The unique identifier for the site."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_connected_sites_id_actions_enable_pixel",
        "method": "POST",
        "path": "/connected-sites/{connected_site_id}/actions/enable-pixel",
        "level": "BASIC",
        "summary": "Enable pixel for connected site",
        "description": "Enable the Mailchimp tracking pixel for a connected site.",
        "group": "connected_sites",
        "path_params": [
            {
                "name": "connected_site_id",
                "type": "str",
                "required": True,
                "description": "The unique identifier for the site."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_connected_sites_id_actions_verify_script_installation",
        "method": "POST",
        "path": "/connected-sites/{connected_site_id}/actions/verify-script-installation",
        "level": "BASIC",
        "summary": "Verify connected site script",
        "description": "Verify that the connected sites script has been installed, either via the script URL or fragment.",
        "group": "connected_sites",
        "path_params": [
            {
                "name": "connected_site_id",
                "type": "str",
                "required": True,
                "description": "The unique identifier for the site."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_conversations",
        "method": "GET",
        "path": "/conversations",
        "level": "READONLY",
        "summary": "List conversations",
        "description": "Get a list of conversations for the account. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.",
        "group": "conversations",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "has_unread_messages",
                "type": "str",
                "required": False,
                "description": "Whether the conversation has any unread messages.",
                "enum": [
                    "True",
                    "False"
                ]
            },
            {
                "name": "list_id",
                "type": "str",
                "required": False,
                "description": "The unique id for the list."
            },
            {
                "name": "campaign_id",
                "type": "str",
                "required": False,
                "description": "The unique id for the campaign."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_conversations_id",
        "method": "GET",
        "path": "/conversations/{conversation_id}",
        "level": "READONLY",
        "summary": "Get conversation",
        "description": "Get details about an individual conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.",
        "group": "conversations",
        "path_params": [
            {
                "name": "conversation_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the conversation."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_conversations_id_messages",
        "method": "GET",
        "path": "/conversations/{conversation_id}/messages",
        "level": "READONLY",
        "summary": "List messages",
        "description": "Get messages from a specific conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.",
        "group": "conversations",
        "path_params": [
            {
                "name": "conversation_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the conversation."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "is_read",
                "type": "str",
                "required": False,
                "description": "Whether a conversation message has been marked as read.",
                "enum": [
                    "True",
                    "False"
                ]
            },
            {
                "name": "before_timestamp",
                "type": "str",
                "required": False,
                "description": "Restrict the response to messages created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_timestamp",
                "type": "str",
                "required": False,
                "description": "Restrict the response to messages created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_conversations_id_messages_id",
        "method": "GET",
        "path": "/conversations/{conversation_id}/messages/{message_id}",
        "level": "READONLY",
        "summary": "Get message",
        "description": "Get an individual message in a conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.",
        "group": "conversations",
        "path_params": [
            {
                "name": "conversation_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the conversation."
            },
            {
                "name": "message_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the conversation message."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_customer_journeys_journeys_id_steps_id_actions_trigger",
        "method": "POST",
        "path": "/customer-journeys/journeys/{journey_id}/steps/{step_id}/actions/trigger",
        "level": "BASIC",
        "summary": "Customer Journeys API trigger for a contact",
        "description": "A step trigger in an Automation flow. To use it, create a starting point or step from the Automation flow builder in the app using the Customer Journey API condition. We’ll provide a url during the process that includes the {journey_id} and {step_id}. You’ll then be able to use this endpoint to trigger the condition for the posted contact.",
        "group": "customer_journeys",
        "path_params": [
            {
                "name": "journey_id",
                "type": "int",
                "required": True,
                "description": "The id for the flow."
            },
            {
                "name": "step_id",
                "type": "int",
                "required": True,
                "description": "The id for the Step."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "email_address"
        ],
        "body_description": "Information about subscribers in a Automation flows's audience. Fields: email_address."
    },
    {
        "name": "get_ecommerce_orders",
        "method": "GET",
        "path": "/ecommerce/orders",
        "level": "READONLY",
        "summary": "List account orders",
        "description": "Get information about an account's orders.",
        "group": "ecommerce",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "campaign_id",
                "type": "str",
                "required": False,
                "description": "Restrict results to orders with a specific `campaign_id` value."
            },
            {
                "name": "outreach_id",
                "type": "str",
                "required": False,
                "description": "Restrict results to orders with a specific `outreach_id` value."
            },
            {
                "name": "customer_id",
                "type": "str",
                "required": False,
                "description": "Restrict results to orders made by a specific customer."
            },
            {
                "name": "has_outreach",
                "type": "bool",
                "required": False,
                "description": "Restrict results to orders that have an outreach attached. For example, an email campaign or Facebook ad."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores",
        "method": "GET",
        "path": "/ecommerce/stores",
        "level": "READONLY",
        "summary": "List stores",
        "description": "Get information about all stores in the account.",
        "group": "ecommerce",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores",
        "method": "POST",
        "path": "/ecommerce/stores",
        "level": "BASIC",
        "summary": "Add store",
        "description": "Add a new store to your Mailchimp account.",
        "group": "ecommerce",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "list_id",
            "name",
            "currency_code"
        ],
        "body_description": "An individual store in an account. Fields: id, list_id, name, platform, domain, is_syncing, email_address, currency_code, money_format, primary_locale, timezone, phone, address."
    },
    {
        "name": "get_ecommerce_stores_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}",
        "level": "READONLY",
        "summary": "Get store info",
        "description": "Get information about a specific store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_ecommerce_stores_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}",
        "level": "ADMIN",
        "summary": "Update store",
        "description": "Update a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "An individual store in an account. Fields: name, platform, domain, is_syncing, email_address, currency_code, money_format, primary_locale, timezone, phone, address."
    },
    {
        "name": "delete_ecommerce_stores_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}",
        "level": "ADMIN",
        "summary": "Delete store",
        "description": "Delete a store. Deleting a store will also delete any associated subresources, including Customers, Orders, Products, and Carts.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_carts",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/carts",
        "level": "READONLY",
        "summary": "List carts",
        "description": "Get information about a store's carts.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_carts",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/carts",
        "level": "BASIC",
        "summary": "Add cart",
        "description": "Add a new cart to a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "currency_code",
            "customer",
            "order_total",
            "lines"
        ],
        "body_description": "Information about a specific cart. Fields: id, customer, campaign_id, checkout_url, currency_code, order_total, tax_total, lines."
    },
    {
        "name": "get_ecommerce_stores_id_carts_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/carts/{cart_id}",
        "level": "READONLY",
        "summary": "Get cart info",
        "description": "Get information about a specific cart.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "cart_id",
                "type": "str",
                "required": True,
                "description": "The id for the cart."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_ecommerce_stores_id_carts_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/carts/{cart_id}",
        "level": "ADMIN",
        "summary": "Update cart",
        "description": "Update a specific cart.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "cart_id",
                "type": "str",
                "required": True,
                "description": "The id for the cart."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about a specific cart. Fields: customer, campaign_id, checkout_url, currency_code, order_total, tax_total, lines."
    },
    {
        "name": "delete_ecommerce_stores_id_carts_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/carts/{cart_id}",
        "level": "ADMIN",
        "summary": "Delete cart",
        "description": "Delete a cart.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "cart_id",
                "type": "str",
                "required": True,
                "description": "The id for the cart."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_carts_id_lines",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/carts/{cart_id}/lines",
        "level": "READONLY",
        "summary": "List cart line items",
        "description": "Get information about a cart's line items.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "cart_id",
                "type": "str",
                "required": True,
                "description": "The id for the cart."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_carts_id_lines",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/carts/{cart_id}/lines",
        "level": "BASIC",
        "summary": "Add cart line item",
        "description": "Add a new line item to an existing cart.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "cart_id",
                "type": "str",
                "required": True,
                "description": "The id for the cart."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "product_id",
            "product_variant_id",
            "quantity",
            "price"
        ],
        "body_description": "Information about a specific cart line item. Fields: id, product_id, product_variant_id, quantity, price."
    },
    {
        "name": "get_ecommerce_stores_id_carts_id_lines_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/carts/{cart_id}/lines/{line_id}",
        "level": "READONLY",
        "summary": "Get cart line item",
        "description": "Get information about a specific cart line item.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "cart_id",
                "type": "str",
                "required": True,
                "description": "The id for the cart."
            },
            {
                "name": "line_id",
                "type": "str",
                "required": True,
                "description": "The id for the line item of a cart."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_ecommerce_stores_id_carts_id_lines_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/carts/{cart_id}/lines/{line_id}",
        "level": "ADMIN",
        "summary": "Update cart line item",
        "description": "Update a specific cart line item.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "cart_id",
                "type": "str",
                "required": True,
                "description": "The id for the cart."
            },
            {
                "name": "line_id",
                "type": "str",
                "required": True,
                "description": "The id for the line item of a cart."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about a specific cart line item. Fields: product_id, product_variant_id, quantity, price."
    },
    {
        "name": "delete_ecommerce_stores_id_carts_lines_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/carts/{cart_id}/lines/{line_id}",
        "level": "ADMIN",
        "summary": "Delete cart line item",
        "description": "Delete a specific cart line item.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "cart_id",
                "type": "str",
                "required": True,
                "description": "The id for the cart."
            },
            {
                "name": "line_id",
                "type": "str",
                "required": True,
                "description": "The id for the line item of a cart."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_customers",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/customers",
        "level": "READONLY",
        "summary": "List customers",
        "description": "Get information about a store's customers.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "email_address",
                "type": "str",
                "required": False,
                "description": "Restrict the response to customers with the email address."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_customers",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/customers",
        "level": "BASIC",
        "summary": "Add customer",
        "description": "Add a new customer to a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "opt_in_status"
        ],
        "body_description": "Information about a specific customer. Fields: id, email_address, sms_phone_number, opt_in_status, company, first_name, last_name, address."
    },
    {
        "name": "get_ecommerce_stores_id_customers_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/customers/{customer_id}",
        "level": "READONLY",
        "summary": "Get customer info",
        "description": "Get information about a specific customer.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "customer_id",
                "type": "str",
                "required": True,
                "description": "The id for the customer of a store."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "put_ecommerce_stores_id_customers_id",
        "method": "PUT",
        "path": "/ecommerce/stores/{store_id}/customers/{customer_id}",
        "level": "ADMIN",
        "summary": "Add or update customer",
        "description": "Add or update a customer.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "customer_id",
                "type": "str",
                "required": True,
                "description": "The id for the customer of a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id"
        ],
        "body_description": "Information about a specific customer. Orders for existing customers should include only the `id` parameter in the `customer` object body. Fields: id, email_address, sms_phone_number, opt_in_status, company, first_name, last_name, address."
    },
    {
        "name": "patch_ecommerce_stores_id_customers_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/customers/{customer_id}",
        "level": "ADMIN",
        "summary": "Update customer",
        "description": "Update a customer.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "customer_id",
                "type": "str",
                "required": True,
                "description": "The id for the customer of a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about a specific customer. Orders for existing customers should include only the `id` parameter in the `customer` object body. Fields: opt_in_status, company, first_name, last_name, address."
    },
    {
        "name": "delete_ecommerce_stores_id_customers_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/customers/{customer_id}",
        "level": "ADMIN",
        "summary": "Delete customer",
        "description": "Delete a customer from a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "customer_id",
                "type": "str",
                "required": True,
                "description": "The id for the customer of a store."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_orders",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/orders",
        "level": "READONLY",
        "summary": "List orders",
        "description": "Get information about a store's orders.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "customer_id",
                "type": "str",
                "required": False,
                "description": "Restrict results to orders made by a specific customer."
            },
            {
                "name": "has_outreach",
                "type": "bool",
                "required": False,
                "description": "Restrict results to orders that have an outreach attached. For example, an email campaign or Facebook ad."
            },
            {
                "name": "campaign_id",
                "type": "str",
                "required": False,
                "description": "Restrict results to orders with a specific `campaign_id` value."
            },
            {
                "name": "outreach_id",
                "type": "str",
                "required": False,
                "description": "Restrict results to orders with a specific `outreach_id` value."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_orders",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/orders",
        "level": "BASIC",
        "summary": "Add order",
        "description": "Add a new order to a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "customer",
            "currency_code",
            "order_total",
            "lines"
        ],
        "body_description": "Information about a specific order. Fields: id, customer, campaign_id, cart_id, landing_site, financial_status, fulfillment_status, currency_code, order_total, order_url, discount_total, tax_total, shipping_total, tracking_code, processed_at_foreign…."
    },
    {
        "name": "get_ecommerce_stores_id_orders_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/orders/{order_id}",
        "level": "READONLY",
        "summary": "Get order info",
        "description": "Get information about a specific order.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "order_id",
                "type": "str",
                "required": True,
                "description": "The id for the order in a store."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "put_ecommerce_stores_id_orders_id",
        "method": "PUT",
        "path": "/ecommerce/stores/{store_id}/orders/{order_id}",
        "level": "ADMIN",
        "summary": "Add or update order",
        "description": "Add or update an order.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "order_id",
                "type": "str",
                "required": True,
                "description": "The id for the order in a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id"
        ],
        "body_description": "Information about a specific order. Fields: id, customer, campaign_id, cart_id, landing_site, financial_status, fulfillment_status, currency_code, order_total, order_url, discount_total, tax_total, shipping_total, tracking_code, processed_at_foreign…."
    },
    {
        "name": "patch_ecommerce_stores_id_orders_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/orders/{order_id}",
        "level": "ADMIN",
        "summary": "Update order",
        "description": "Update a specific order.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "order_id",
                "type": "str",
                "required": True,
                "description": "The id for the order in a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about a specific order. Fields: customer, campaign_id, cart_id, landing_site, financial_status, fulfillment_status, currency_code, order_total, order_url, discount_total, tax_total, shipping_total, tracking_code, processed_at_foreign, cancelled_at_foreign…."
    },
    {
        "name": "delete_ecommerce_stores_id_orders_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/orders/{order_id}",
        "level": "ADMIN",
        "summary": "Delete order",
        "description": "Delete an order.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "order_id",
                "type": "str",
                "required": True,
                "description": "The id for the order in a store."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_orders_id_lines",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/orders/{order_id}/lines",
        "level": "READONLY",
        "summary": "List order line items",
        "description": "Get information about an order's line items.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "order_id",
                "type": "str",
                "required": True,
                "description": "The id for the order in a store."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_orders_id_lines",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/orders/{order_id}/lines",
        "level": "BASIC",
        "summary": "Add order line item",
        "description": "Add a new line item to an existing order.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "order_id",
                "type": "str",
                "required": True,
                "description": "The id for the order in a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "product_id",
            "product_variant_id",
            "quantity",
            "price"
        ],
        "body_description": "Information about a specific order line. Fields: id, product_id, product_variant_id, product, quantity, price, discount."
    },
    {
        "name": "get_ecommerce_stores_id_orders_id_lines_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/orders/{order_id}/lines/{line_id}",
        "level": "READONLY",
        "summary": "Get order line item",
        "description": "Get information about a specific order line item.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "order_id",
                "type": "str",
                "required": True,
                "description": "The id for the order in a store."
            },
            {
                "name": "line_id",
                "type": "str",
                "required": True,
                "description": "The id for the line item of an order."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_ecommerce_stores_id_orders_id_lines_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/orders/{order_id}/lines/{line_id}",
        "level": "ADMIN",
        "summary": "Update order line item",
        "description": "Update a specific order line item.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "order_id",
                "type": "str",
                "required": True,
                "description": "The id for the order in a store."
            },
            {
                "name": "line_id",
                "type": "str",
                "required": True,
                "description": "The id for the line item of an order."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about a specific order line. Fields: product_id, product_variant_id, quantity, price, discount."
    },
    {
        "name": "delete_ecommerce_stores_id_orders_id_lines_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/orders/{order_id}/lines/{line_id}",
        "level": "ADMIN",
        "summary": "Delete order line item",
        "description": "Delete a specific order line item.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "order_id",
                "type": "str",
                "required": True,
                "description": "The id for the order in a store."
            },
            {
                "name": "line_id",
                "type": "str",
                "required": True,
                "description": "The id for the line item of an order."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_products",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/products",
        "level": "READONLY",
        "summary": "List product",
        "description": "Get information about a store's products.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_products",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/products",
        "level": "BASIC",
        "summary": "Add product",
        "description": "Add a new product to a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "title",
            "variants"
        ],
        "body_description": "Information about a specific product. Fields: id, title, handle, url, description, type, vendor, image_url, variants, images, published_at_foreign."
    },
    {
        "name": "get_ecommerce_stores_id_products_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}",
        "level": "READONLY",
        "summary": "Get product info",
        "description": "Get information about a specific product.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "put_ecommerce_stores_id_products_id",
        "method": "PUT",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}",
        "level": "ADMIN",
        "summary": "Create or update product",
        "description": "Update a specific product.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id"
        ],
        "body_description": "Information about a specific product. Fields: id, title, handle, url, description, type, vendor, image_url, variants, images, published_at_foreign."
    },
    {
        "name": "patch_ecommerce_stores_id_products_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}",
        "level": "ADMIN",
        "summary": "Update product",
        "description": "Update a specific product.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about a specific product. Fields: title, handle, url, description, type, vendor, image_url, variants, images, published_at_foreign."
    },
    {
        "name": "delete_ecommerce_stores_id_products_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}",
        "level": "ADMIN",
        "summary": "Delete product",
        "description": "Delete a product.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_products_id_images",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/images",
        "level": "READONLY",
        "summary": "List product images",
        "description": "Get information about a product's images.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_products_id_images",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/images",
        "level": "BASIC",
        "summary": "Add product image",
        "description": "Add a new image to the product.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "url"
        ],
        "body_description": "Information about a specific product image. Fields: id, url, variant_ids."
    },
    {
        "name": "get_ecommerce_stores_id_products_id_images_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/images/{image_id}",
        "level": "READONLY",
        "summary": "Get product image info",
        "description": "Get information about a specific product image.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            },
            {
                "name": "image_id",
                "type": "str",
                "required": True,
                "description": "The id for the product image."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_ecommerce_stores_id_products_id_images_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/images/{image_id}",
        "level": "ADMIN",
        "summary": "Update product image",
        "description": "Update a product image.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            },
            {
                "name": "image_id",
                "type": "str",
                "required": True,
                "description": "The id for the product image."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about a specific product image. Fields: id, url, variant_ids."
    },
    {
        "name": "delete_ecommerce_stores_id_products_id_images_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/images/{image_id}",
        "level": "ADMIN",
        "summary": "Delete product image",
        "description": "Delete a product image.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            },
            {
                "name": "image_id",
                "type": "str",
                "required": True,
                "description": "The id for the product image."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_products_id_variants",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/variants",
        "level": "READONLY",
        "summary": "List product variants",
        "description": "Get information about a product's variants.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_products_id_variants",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/variants",
        "level": "BASIC",
        "summary": "Add product variant",
        "description": "Add a new variant to the product.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "title"
        ],
        "body_description": "Information about a specific product variant. Fields: id, title, url, sku, price, inventory_quantity, image_url, backorders, visibility."
    },
    {
        "name": "get_ecommerce_stores_id_products_id_variants_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/variants/{variant_id}",
        "level": "READONLY",
        "summary": "Get product variant info",
        "description": "Get information about a specific product variant.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            },
            {
                "name": "variant_id",
                "type": "str",
                "required": True,
                "description": "The id for the product variant."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "put_ecommerce_stores_id_products_id_variants_id",
        "method": "PUT",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/variants/{variant_id}",
        "level": "ADMIN",
        "summary": "Add or update product variant",
        "description": "Add or update a product variant.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            },
            {
                "name": "variant_id",
                "type": "str",
                "required": True,
                "description": "The id for the product variant."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "title"
        ],
        "body_description": "Information about a specific product variant. Fields: id, title, url, sku, price, inventory_quantity, image_url, backorders, visibility."
    },
    {
        "name": "patch_ecommerce_stores_id_products_id_variants_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/variants/{variant_id}",
        "level": "ADMIN",
        "summary": "Update product variant",
        "description": "Update a product variant.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            },
            {
                "name": "variant_id",
                "type": "str",
                "required": True,
                "description": "The id for the product variant."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about a specific product variant. Fields: title, url, sku, price, inventory_quantity, image_url, backorders, visibility."
    },
    {
        "name": "delete_ecommerce_stores_id_products_id_variants_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/products/{product_id}/variants/{variant_id}",
        "level": "ADMIN",
        "summary": "Delete product variant",
        "description": "Delete a product variant.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "product_id",
                "type": "str",
                "required": True,
                "description": "The id for the product of a store."
            },
            {
                "name": "variant_id",
                "type": "str",
                "required": True,
                "description": "The id for the product variant."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_promorules",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/promo-rules",
        "level": "READONLY",
        "summary": "List promo rules",
        "description": "Get information about a store's promo rules.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_promorules",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/promo-rules",
        "level": "BASIC",
        "summary": "Add promo rule",
        "description": "Add a new promo rule to a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "description",
            "amount",
            "type",
            "target"
        ],
        "body_description": "Information about an Ecommerce Store's specific Promo Rule. Fields: id, title, description, starts_at, ends_at, amount, type, target, enabled, created_at_foreign, updated_at_foreign."
    },
    {
        "name": "get_ecommerce_stores_id_promorules_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}",
        "level": "READONLY",
        "summary": "Get promo rule",
        "description": "Get information about a specific promo rule.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "promo_rule_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo rule of a store."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_ecommerce_stores_id_promorules_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}",
        "level": "ADMIN",
        "summary": "Update promo rule",
        "description": "Update a promo rule.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "promo_rule_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo rule of a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about an Ecommerce Store's specific Promo Rule. Fields: title, description, starts_at, ends_at, amount, type, target, enabled, created_at_foreign, updated_at_foreign."
    },
    {
        "name": "delete_ecommerce_stores_id_promorules_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}",
        "level": "ADMIN",
        "summary": "Delete promo rule",
        "description": "Delete a promo rule from a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "promo_rule_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo rule of a store."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ecommerce_stores_id_promocodes",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}/promo-codes",
        "level": "READONLY",
        "summary": "List promo codes",
        "description": "Get information about a store's promo codes.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "promo_rule_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo rule of a store."
            },
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_ecommerce_stores_id_promocodes",
        "method": "POST",
        "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}/promo-codes",
        "level": "BASIC",
        "summary": "Add promo code",
        "description": "Add a new promo code to a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "promo_rule_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo rule of a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "id",
            "code",
            "redemption_url"
        ],
        "body_description": "Information about an Ecommerce Store's specific Promo Code. Fields: id, code, redemption_url, usage_count, enabled, created_at_foreign, updated_at_foreign."
    },
    {
        "name": "get_ecommerce_stores_id_promocodes_id",
        "method": "GET",
        "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}/promo-codes/{promo_code_id}",
        "level": "READONLY",
        "summary": "Get promo code",
        "description": "Get information about a specific promo code.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "promo_rule_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo rule of a store."
            },
            {
                "name": "promo_code_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo code of a store."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_ecommerce_stores_id_promocodes_id",
        "method": "PATCH",
        "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}/promo-codes/{promo_code_id}",
        "level": "ADMIN",
        "summary": "Update promo code",
        "description": "Update a promo code.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "promo_rule_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo rule of a store."
            },
            {
                "name": "promo_code_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo code of a store."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about an Ecommerce Store's specific Promo Code. Fields: code, redemption_url, usage_count, enabled, created_at_foreign, updated_at_foreign."
    },
    {
        "name": "delete_ecommerce_stores_id_promocodes_id",
        "method": "DELETE",
        "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}/promo-codes/{promo_code_id}",
        "level": "ADMIN",
        "summary": "Delete promo code",
        "description": "Delete a promo code from a store.",
        "group": "ecommerce",
        "path_params": [
            {
                "name": "store_id",
                "type": "str",
                "required": True,
                "description": "The store id."
            },
            {
                "name": "promo_rule_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo rule of a store."
            },
            {
                "name": "promo_code_id",
                "type": "str",
                "required": True,
                "description": "The id for the promo code of a store."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_all_facebook_ads",
        "method": "GET",
        "path": "/facebook-ads",
        "level": "READONLY",
        "summary": "List facebook ads",
        "description": "Get list of Facebook ads.",
        "group": "facebook_ads",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "created_at",
                    "updated_at",
                    "end_time"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_facebook_ads_id",
        "method": "GET",
        "path": "/facebook-ads/{outreach_id}",
        "level": "READONLY",
        "summary": "Get facebook ad info",
        "description": "Get details of a Facebook ad.",
        "group": "facebook_ads",
        "path_params": [
            {
                "name": "outreach_id",
                "type": "str",
                "required": True,
                "description": "The outreach id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_file_manager_files",
        "method": "GET",
        "path": "/file-manager/files",
        "level": "READONLY",
        "summary": "List stored files",
        "description": "Get a list of available images and files stored in the File Manager for the account.",
        "group": "file_manager",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "type",
                "type": "str",
                "required": False,
                "description": "The file type for the File Manager file."
            },
            {
                "name": "created_by",
                "type": "str",
                "required": False,
                "description": "The Mailchimp account user who created the File Manager file."
            },
            {
                "name": "before_created_at",
                "type": "str",
                "required": False,
                "description": "Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_created_at",
                "type": "str",
                "required": False,
                "description": "Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "added_date",
                    "name",
                    "size"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_file_manager_files",
        "method": "POST",
        "path": "/file-manager/files",
        "level": "BASIC",
        "summary": "Add file",
        "description": "Upload a new image or file to the File Manager.",
        "group": "file_manager",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name",
            "file_data"
        ],
        "body_description": "An individual file listed in the File Manager. Fields: folder_id, name, file_data."
    },
    {
        "name": "get_file_manager_files_id",
        "method": "GET",
        "path": "/file-manager/files/{file_id}",
        "level": "READONLY",
        "summary": "Get file",
        "description": "Get information about a specific file in the File Manager.",
        "group": "file_manager",
        "path_params": [
            {
                "name": "file_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the File Manager file."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_file_manager_files_id",
        "method": "PATCH",
        "path": "/file-manager/files/{file_id}",
        "level": "ADMIN",
        "summary": "Update file",
        "description": "Update a file in the File Manager.",
        "group": "file_manager",
        "path_params": [
            {
                "name": "file_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the File Manager file."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "An individual file listed in the File Manager. Fields: folder_id, name."
    },
    {
        "name": "delete_file_manager_files_id",
        "method": "DELETE",
        "path": "/file-manager/files/{file_id}",
        "level": "ADMIN",
        "summary": "Delete file",
        "description": "Remove a specific file from the File Manager.",
        "group": "file_manager",
        "path_params": [
            {
                "name": "file_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the File Manager file."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_file_manager_folders",
        "method": "GET",
        "path": "/file-manager/folders",
        "level": "READONLY",
        "summary": "List folders",
        "description": "Get a list of all folders in the File Manager.",
        "group": "file_manager",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "created_by",
                "type": "str",
                "required": False,
                "description": "The Mailchimp account user who created the File Manager file."
            },
            {
                "name": "before_created_at",
                "type": "str",
                "required": False,
                "description": "Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_created_at",
                "type": "str",
                "required": False,
                "description": "Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_file_manager_folders",
        "method": "POST",
        "path": "/file-manager/folders",
        "level": "BASIC",
        "summary": "Add folder",
        "description": "Create a new folder in the File Manager.",
        "group": "file_manager",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "An individual folder listed in the File Manager. Fields: name."
    },
    {
        "name": "get_file_manager_folders_id",
        "method": "GET",
        "path": "/file-manager/folders/{folder_id}",
        "level": "READONLY",
        "summary": "Get folder",
        "description": "Get information about a specific folder in the File Manager.",
        "group": "file_manager",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the File Manager folder."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_file_manager_folders_id",
        "method": "PATCH",
        "path": "/file-manager/folders/{folder_id}",
        "level": "ADMIN",
        "summary": "Update folder",
        "description": "Update a specific File Manager folder.",
        "group": "file_manager",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the File Manager folder."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "An individual folder listed in the File Manager. Fields: name."
    },
    {
        "name": "delete_file_manager_folders_id",
        "method": "DELETE",
        "path": "/file-manager/folders/{folder_id}",
        "level": "ADMIN",
        "summary": "Delete folder",
        "description": "Delete a specific folder in the File Manager.",
        "group": "file_manager",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the File Manager folder."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_file_manager_folders_files",
        "method": "GET",
        "path": "/file-manager/folders/{folder_id}/files",
        "level": "READONLY",
        "summary": "List stored files",
        "description": "Get a list of available images and files stored in this folder.",
        "group": "file_manager",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the File Manager folder."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "type",
                "type": "str",
                "required": False,
                "description": "The file type for the File Manager file."
            },
            {
                "name": "created_by",
                "type": "str",
                "required": False,
                "description": "The Mailchimp account user who created the File Manager file."
            },
            {
                "name": "before_created_at",
                "type": "str",
                "required": False,
                "description": "Restrict the response to files created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_created_at",
                "type": "str",
                "required": False,
                "description": "Restrict the response to files created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "added_date",
                    "name",
                    "size"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_all_landing_pages",
        "method": "GET",
        "path": "/landing-pages",
        "level": "READONLY",
        "summary": "List landing pages",
        "description": "Get all landing pages.",
        "group": "landing_pages",
        "path_params": [],
        "query_params": [
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "created_at",
                    "updated_at"
                ]
            },
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_all_landing_pages",
        "method": "POST",
        "path": "/landing-pages",
        "level": "BASIC",
        "summary": "Add landing page",
        "description": "Create an unpublished and contentless Mailchimp landing page.",
        "group": "landing_pages",
        "path_params": [],
        "query_params": [
            {
                "name": "use_default_list",
                "type": "bool",
                "required": False,
                "description": "Will create the Landing Page using the account's Default List instead of requiring a list_id."
            }
        ],
        "has_body": True,
        "body_required": [],
        "body_description": "A summary of an individual page's properties. Fields: name, title, description, store_id, list_id, type, template_id, tracking."
    },
    {
        "name": "get_landing_page_id",
        "method": "GET",
        "path": "/landing-pages/{page_id}",
        "level": "READONLY",
        "summary": "Get landing page info",
        "description": "Get information about a specific page.",
        "group": "landing_pages",
        "path_params": [
            {
                "name": "page_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the page."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_landing_page_id",
        "method": "PATCH",
        "path": "/landing-pages/{page_id}",
        "level": "ADMIN",
        "summary": "Update landing page",
        "description": "Update a landing page.",
        "group": "landing_pages",
        "path_params": [
            {
                "name": "page_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the page."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "A summary of an individual page's properties. Fields: name, title, description, store_id, list_id, tracking."
    },
    {
        "name": "delete_landing_page_id",
        "method": "DELETE",
        "path": "/landing-pages/{page_id}",
        "level": "ADMIN",
        "summary": "Delete landing page",
        "description": "Delete a landing page.",
        "group": "landing_pages",
        "path_params": [
            {
                "name": "page_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the page."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_landing_page_id_actions_publish",
        "method": "POST",
        "path": "/landing-pages/{page_id}/actions/publish",
        "level": "BASIC",
        "summary": "Publish landing page",
        "description": "Publish a landing page that is in draft, unpublished, or has been previously published and edited.",
        "group": "landing_pages",
        "path_params": [
            {
                "name": "page_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the page."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_landing_page_id_actions_unpublish",
        "method": "POST",
        "path": "/landing-pages/{page_id}/actions/unpublish",
        "level": "BASIC",
        "summary": "Unpublish landing page",
        "description": "Unpublish a landing page that is in draft or has been published.",
        "group": "landing_pages",
        "path_params": [
            {
                "name": "page_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the page."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_landing_page_id_content",
        "method": "GET",
        "path": "/landing-pages/{page_id}/content",
        "level": "READONLY",
        "summary": "Get landing page content",
        "description": "Get the the HTML for your landing page.",
        "group": "landing_pages",
        "path_params": [
            {
                "name": "page_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the page."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists",
        "method": "GET",
        "path": "/lists",
        "level": "READONLY",
        "summary": "Get lists info",
        "description": "Get information about all lists in the account.",
        "group": "lists",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "before_date_created",
                "type": "str",
                "required": False,
                "description": "Restrict response to lists created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_date_created",
                "type": "str",
                "required": False,
                "description": "Restrict results to lists created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "before_campaign_last_sent",
                "type": "str",
                "required": False,
                "description": "Restrict results to lists created before the last campaign send date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_campaign_last_sent",
                "type": "str",
                "required": False,
                "description": "Restrict results to lists created after the last campaign send date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "email",
                "type": "str",
                "required": False,
                "description": "Restrict results to lists that include a specific subscriber's email address."
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "date_created"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            },
            {
                "name": "has_ecommerce_store",
                "type": "bool",
                "required": False,
                "description": "Restrict results to lists that contain an active, connected, undeleted ecommerce store."
            },
            {
                "name": "include_total_contacts",
                "type": "bool",
                "required": False,
                "description": "Deprecated. Return the total_contacts field in the stats response, which contains an approximate count of subscribed, unsubscribed, and transactional contacts. For a complete audience contact count, use the /audiences…"
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists",
        "method": "POST",
        "path": "/lists",
        "level": "BASIC",
        "summary": "Add list",
        "description": "Create a new list in your Mailchimp account.",
        "group": "lists",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name",
            "permission_reminder",
            "email_type_option",
            "contact",
            "campaign_defaults"
        ],
        "body_description": "Information about a specific list. Fields: name, contact, permission_reminder, use_archive_bar, campaign_defaults, notify_on_subscribe, notify_on_unsubscribe, email_type_option, double_optin, marketing_permissions."
    },
    {
        "name": "get_lists_id",
        "method": "GET",
        "path": "/lists/{list_id}",
        "level": "READONLY",
        "summary": "Get list info",
        "description": "Get information about a specific list in your Mailchimp account. Results include list members who have signed up but haven't confirmed their subscription yet and unsubscribed or cleaned.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "include_total_contacts",
                "type": "bool",
                "required": False,
                "description": "Deprecated. Return the total_contacts field in the stats response, which contains an approximate count of subscribed, unsubscribed, and transactional contacts. For a complete audience contact count, use the /audiences…"
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id",
        "method": "POST",
        "path": "/lists/{list_id}",
        "level": "BASIC",
        "summary": "Batch subscribe or unsubscribe",
        "description": "Batch subscribe or unsubscribe list members.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "skip_merge_validation",
                "type": "bool",
                "required": False,
                "description": "If skip_merge_validation is True, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to False."
            },
            {
                "name": "skip_duplicate_check",
                "type": "bool",
                "required": False,
                "description": "If skip_duplicate_check is True, we will ignore duplicates sent in the request when using the batch sub/unsub on the lists endpoint. The status of the first appearance in the request will be saved. This defaults to…"
            }
        ],
        "has_body": True,
        "body_required": [
            "members"
        ],
        "body_description": "Members to subscribe to or unsubscribe from a list. Fields: members, sync_tags, update_existing."
    },
    {
        "name": "patch_lists_id",
        "method": "PATCH",
        "path": "/lists/{list_id}",
        "level": "ADMIN",
        "summary": "Update lists",
        "description": "Update the settings for a specific list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Information about a specific list. Fields: name, contact, permission_reminder, use_archive_bar, campaign_defaults, notify_on_subscribe, notify_on_unsubscribe, email_type_option, double_optin, marketing_permissions."
    },
    {
        "name": "delete_lists_id",
        "method": "DELETE",
        "path": "/lists/{list_id}",
        "level": "ADMIN",
        "summary": "Delete list",
        "description": "Delete a list from your Mailchimp account. If you delete a list, you'll lose the list history—including subscriber activity, unsubscribes, complaints, and bounces. You’ll also lose subscribers’ email addresses, unless you exported and backed up your list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_abuse_reports",
        "method": "GET",
        "path": "/lists/{list_id}/abuse-reports",
        "level": "READONLY",
        "summary": "List abuse reports",
        "description": "Get all abuse reports for a specific list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_abuse_reports_id",
        "method": "GET",
        "path": "/lists/{list_id}/abuse-reports/{report_id}",
        "level": "READONLY",
        "summary": "Get abuse report",
        "description": "Get details about a specific abuse report.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "report_id",
                "type": "str",
                "required": True,
                "description": "The id for the abuse report."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_activity",
        "method": "GET",
        "path": "/lists/{list_id}/activity",
        "level": "READONLY",
        "summary": "List recent activity",
        "description": "Get up to the previous 180 days of daily detailed aggregated activity stats for a list, not including Automation activity.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_clients",
        "method": "GET",
        "path": "/lists/{list_id}/clients",
        "level": "READONLY",
        "summary": "List top email clients",
        "description": "Get a list of the top email clients based on user-agent strings.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_growth_history",
        "method": "GET",
        "path": "/lists/{list_id}/growth-history",
        "level": "READONLY",
        "summary": "List growth history data",
        "description": "Get a month-by-month summary of a specific list's growth activity.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "month"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_growth_history_id",
        "method": "GET",
        "path": "/lists/{list_id}/growth-history/{month}",
        "level": "READONLY",
        "summary": "Get growth history by month",
        "description": "Get a summary of a specific list's growth activity for a specific month and year.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "month",
                "type": "str",
                "required": True,
                "description": "A specific month of list growth history."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_interest_categories",
        "method": "GET",
        "path": "/lists/{list_id}/interest-categories",
        "level": "READONLY",
        "summary": "List interest categories",
        "description": "Get information about a list's interest categories.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "type",
                "type": "str",
                "required": False,
                "description": "Restrict results a type of interest group"
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns interest categories sorted by the specified field. Defaults to display_order.",
                "enum": [
                    "name",
                    "display_order"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_interest_categories",
        "method": "POST",
        "path": "/lists/{list_id}/interest-categories",
        "level": "BASIC",
        "summary": "Add interest category",
        "description": "Create a new interest category.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "title",
            "type"
        ],
        "body_description": "Interest categories organize interests, which are used to group subscribers based on their preferences. These correspond to Group Titles the application. Fields: title, display_order, type."
    },
    {
        "name": "get_lists_id_interest_categories_id",
        "method": "GET",
        "path": "/lists/{list_id}/interest-categories/{interest_category_id}",
        "level": "READONLY",
        "summary": "Get interest category info",
        "description": "Get information about a specific interest category.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "interest_category_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the interest category."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_lists_id_interest_categories_id",
        "method": "PATCH",
        "path": "/lists/{list_id}/interest-categories/{interest_category_id}",
        "level": "ADMIN",
        "summary": "Update interest category",
        "description": "Update a specific interest category.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "interest_category_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the interest category."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Interest categories organize interests, which are used to group subscribers based on their preferences. These correspond to Group Titles the application. Fields: title, display_order, type."
    },
    {
        "name": "delete_lists_id_interest_categories_id",
        "method": "DELETE",
        "path": "/lists/{list_id}/interest-categories/{interest_category_id}",
        "level": "ADMIN",
        "summary": "Delete interest category",
        "description": "Delete a specific interest category.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "interest_category_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the interest category."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_interest_categories_id_interests",
        "method": "GET",
        "path": "/lists/{list_id}/interest-categories/{interest_category_id}/interests",
        "level": "READONLY",
        "summary": "List interests in category",
        "description": "Get a list of this category's interests.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "interest_category_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the interest category."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_interest_categories_id_interests",
        "method": "POST",
        "path": "/lists/{list_id}/interest-categories/{interest_category_id}/interests",
        "level": "BASIC",
        "summary": "Add interest in category",
        "description": "Create a new interest or 'group name' for a specific category.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "interest_category_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the interest category."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "Assign subscribers to interests to group them together. Interests are referred to as 'group names' in the Mailchimp application. Fields: name, display_order."
    },
    {
        "name": "get_lists_id_interest_categories_id_interests_id",
        "method": "GET",
        "path": "/lists/{list_id}/interest-categories/{interest_category_id}/interests/{interest_id}",
        "level": "READONLY",
        "summary": "Get interest in category",
        "description": "Get interests or 'group names' for a specific category.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "interest_category_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the interest category."
            },
            {
                "name": "interest_id",
                "type": "str",
                "required": True,
                "description": "The specific interest or 'group name'."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_lists_id_interest_categories_id_interests_id",
        "method": "PATCH",
        "path": "/lists/{list_id}/interest-categories/{interest_category_id}/interests/{interest_id}",
        "level": "ADMIN",
        "summary": "Update interest in category",
        "description": "Update interests or 'group names' for a specific category.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "interest_category_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the interest category."
            },
            {
                "name": "interest_id",
                "type": "str",
                "required": True,
                "description": "The specific interest or 'group name'."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Assign subscribers to interests to group them together. Interests are referred to as 'group names' in the Mailchimp application. Fields: name, display_order."
    },
    {
        "name": "delete_lists_id_interest_categories_id_interests_id",
        "method": "DELETE",
        "path": "/lists/{list_id}/interest-categories/{interest_category_id}/interests/{interest_id}",
        "level": "ADMIN",
        "summary": "Delete interest in category",
        "description": "Delete interests or group names in a specific category.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "interest_category_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the interest category."
            },
            {
                "name": "interest_id",
                "type": "str",
                "required": True,
                "description": "The specific interest or 'group name'."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_locations",
        "method": "GET",
        "path": "/lists/{list_id}/locations",
        "level": "READONLY",
        "summary": "List locations",
        "description": "Get the locations (countries) that the list's subscribers have been tagged to based on geocoding their IP address.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_members",
        "method": "GET",
        "path": "/lists/{list_id}/members",
        "level": "READONLY",
        "summary": "List members info",
        "description": "Get information about members in a specific Mailchimp list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "email_type",
                "type": "str",
                "required": False,
                "description": "The email type."
            },
            {
                "name": "status",
                "type": "str",
                "required": False,
                "description": "The subscriber's status.",
                "enum": [
                    "subscribed",
                    "unsubscribed",
                    "cleaned",
                    "pending",
                    "transactional",
                    "archived"
                ]
            },
            {
                "name": "since_timestamp_opt",
                "type": "str",
                "required": False,
                "description": "Restrict results to subscribers who opted-in after the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "before_timestamp_opt",
                "type": "str",
                "required": False,
                "description": "Restrict results to subscribers who opted-in before the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_last_changed",
                "type": "str",
                "required": False,
                "description": "Restrict results to subscribers whose information changed after the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "before_last_changed",
                "type": "str",
                "required": False,
                "description": "Restrict results to subscribers whose information changed before the set timeframe. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "unique_email_id",
                "type": "str",
                "required": False,
                "description": "A unique identifier for the email address across all Mailchimp lists."
            },
            {
                "name": "vip_only",
                "type": "bool",
                "required": False,
                "description": "A filter to return only the list's VIP members. Passing `True` will restrict results to VIP list members, passing `False` will return all list members."
            },
            {
                "name": "interest_category_id",
                "type": "str",
                "required": False,
                "description": "The unique id for the interest category."
            },
            {
                "name": "interest_ids",
                "type": "str",
                "required": False,
                "description": "Used to filter list members by interests. Must be accompanied by interest_category_id and interest_match. The value must be a comma separated list of interest ids present for any supplied interest categories."
            },
            {
                "name": "interest_match",
                "type": "str",
                "required": False,
                "description": "Used to filter list members by interests. Must be accompanied by interest_category_id and interest_ids. \"any\" will match a member with any of the interest supplied, \"all\" will only match members with every interest…",
                "enum": [
                    "any",
                    "all",
                    "none"
                ]
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "timestamp_opt",
                    "timestamp_signup",
                    "last_changed"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            },
            {
                "name": "since_last_campaign",
                "type": "bool",
                "required": False,
                "description": "Filter subscribers by those subscribed/unsubscribed/pending/cleaned since last email campaign send. Member status is required to use this filter."
            },
            {
                "name": "unsubscribed_since",
                "type": "str",
                "required": False,
                "description": "Filter subscribers by those unsubscribed since a specific date. Using any status other than unsubscribed with this filter will result in an error."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_members",
        "method": "POST",
        "path": "/lists/{list_id}/members",
        "level": "BASIC",
        "summary": "Add member to list",
        "description": "Add a new member to the list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "skip_merge_validation",
                "type": "bool",
                "required": False,
                "description": "If skip_merge_validation is True, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to False."
            }
        ],
        "has_body": True,
        "body_required": [
            "email_address",
            "status"
        ],
        "body_description": "Individuals who are currently or have been previously subscribed to this list, including members who have bounced or unsubscribed. Fields: email_address, email_type, status, merge_fields, interests, language, vip, location, marketing_permissions, ip_signup, timestamp_signup, ip_opt, timestamp_opt, tags."
    },
    {
        "name": "get_lists_id_members_id",
        "method": "GET",
        "path": "/lists/{list_id}/members/{subscriber_hash}",
        "level": "READONLY",
        "summary": "Get member info",
        "description": "Get information about a specific list member, including a currently subscribed, unsubscribed, or bounced member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "put_lists_id_members_id",
        "method": "PUT",
        "path": "/lists/{list_id}/members/{subscriber_hash}",
        "level": "ADMIN",
        "summary": "Add or update list member",
        "description": "Add or update a list member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [
            {
                "name": "skip_merge_validation",
                "type": "bool",
                "required": False,
                "description": "If skip_merge_validation is True, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to False."
            }
        ],
        "has_body": True,
        "body_required": [
            "email_address",
            "status_if_new"
        ],
        "body_description": "Individuals who are currently or have been previously subscribed to this list, including members who have bounced or unsubscribed. Fields: email_address, status_if_new, email_type, status, merge_fields, interests, language, vip, location, marketing_permissions, ip_signup, timestamp_signup, ip_opt, timestamp_opt."
    },
    {
        "name": "patch_lists_id_members_id",
        "method": "PATCH",
        "path": "/lists/{list_id}/members/{subscriber_hash}",
        "level": "ADMIN",
        "summary": "Update list member",
        "description": "Update information for a specific list member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [
            {
                "name": "skip_merge_validation",
                "type": "bool",
                "required": False,
                "description": "If skip_merge_validation is True, member data will be accepted without merge field values, even if the merge field is usually required. This defaults to False."
            }
        ],
        "has_body": True,
        "body_required": [],
        "body_description": "Individuals who are currently or have been previously subscribed to this list, including members who have bounced or unsubscribed. Fields: email_address, email_type, status, merge_fields, interests, language, vip, location, marketing_permissions, ip_signup, timestamp_signup, ip_opt, timestamp_opt."
    },
    {
        "name": "delete_lists_id_members_id",
        "method": "DELETE",
        "path": "/lists/{list_id}/members/{subscriber_hash}",
        "level": "ADMIN",
        "summary": "Archive list member",
        "description": "Archive a list member. To permanently delete, use the delete-permanent action.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_members_hash_actions_delete_permanent",
        "method": "POST",
        "path": "/lists/{list_id}/members/{subscriber_hash}/actions/delete-permanent",
        "level": "BASIC",
        "summary": "Delete list member",
        "description": "Delete all personally identifiable information related to a list member, and remove them from a list. This will make it impossible to re-import the list member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_members_id_activity",
        "method": "GET",
        "path": "/lists/{list_id}/members/{subscriber_hash}/activity",
        "level": "READONLY",
        "summary": "View recent activity 50",
        "description": "Get the last 50 events of a member's activity on a specific list, including opens, clicks, and unsubscribes.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "action",
                "type": "str",
                "required": False,
                "description": "A comma seperated list of actions to return.",
                "enum": [
                    "abuse",
                    "bounce",
                    "click",
                    "open",
                    "sent",
                    "unsub",
                    "ecomm"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_members_id_activity_feed",
        "method": "GET",
        "path": "/lists/{list_id}/members/{subscriber_hash}/activity-feed",
        "level": "READONLY",
        "summary": "View recent activity",
        "description": "Get a member's activity on a specific list, including opens, clicks, and unsubscribes.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "activity_filters",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of activity filters that correspond to a set of activity types, e.g \"?activity_filters=open,bounce,click\".",
                "enum": [
                    "bounce",
                    "click",
                    "conversation",
                    "ecommerce_signup",
                    "event",
                    "web_engagement",
                    "generic_signup",
                    "landing_page_signup",
                    "marketing_permission",
                    "note",
                    "open",
                    "order",
                    "postcard_sent",
                    "sent",
                    "signup",
                    "squatter_signup",
                    "unsub",
                    "website_signup",
                    "survey_response",
                    "sms_bulk_sent",
                    "inbox_thread",
                    "qbo_payment_link",
                    "video_call_transcripts",
                    "whatsapp_bulk_sent",
                    "whatsapp_delivered"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_members_id_events",
        "method": "GET",
        "path": "/lists/{list_id}/members/{subscriber_hash}/events",
        "level": "READONLY",
        "summary": "List member events",
        "description": "Get events for a contact.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_list_member_events",
        "method": "POST",
        "path": "/lists/{list_id}/members/{subscriber_hash}/events",
        "level": "BASIC",
        "summary": "Add event",
        "description": "Add an event for a list member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "A new event for a specific list member Fields: name, properties, is_syncing, occurred_at."
    },
    {
        "name": "get_lists_id_members_id_goals",
        "method": "GET",
        "path": "/lists/{list_id}/members/{subscriber_hash}/goals",
        "level": "READONLY",
        "summary": "List member goal events",
        "description": "Get the last 50 Goal events for a member on a specific list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_members_id_notes",
        "method": "GET",
        "path": "/lists/{list_id}/members/{subscriber_hash}/notes",
        "level": "READONLY",
        "summary": "List recent member notes",
        "description": "Get recent notes for a specific list member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns notes sorted by the specified field.",
                "enum": [
                    "created_at",
                    "updated_at",
                    "note_id"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            },
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_members_id_notes",
        "method": "POST",
        "path": "/lists/{list_id}/members/{subscriber_hash}/notes",
        "level": "BASIC",
        "summary": "Add member note",
        "description": "Add a new note for a specific subscriber.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "A specific note for a specific member. Fields: note."
    },
    {
        "name": "get_lists_id_members_id_notes_id",
        "method": "GET",
        "path": "/lists/{list_id}/members/{subscriber_hash}/notes/{note_id}",
        "level": "READONLY",
        "summary": "Get member note",
        "description": "Get a specific note for a specific list member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            },
            {
                "name": "note_id",
                "type": "str",
                "required": True,
                "description": "The id for the note."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_lists_id_members_id_notes_id",
        "method": "PATCH",
        "path": "/lists/{list_id}/members/{subscriber_hash}/notes/{note_id}",
        "level": "ADMIN",
        "summary": "Update note",
        "description": "Update a specific note for a specific list member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            },
            {
                "name": "note_id",
                "type": "str",
                "required": True,
                "description": "The id for the note."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "A specific note for a specific member. Fields: note."
    },
    {
        "name": "delete_lists_id_members_id_notes_id",
        "method": "DELETE",
        "path": "/lists/{list_id}/members/{subscriber_hash}/notes/{note_id}",
        "level": "ADMIN",
        "summary": "Delete note",
        "description": "Delete a specific note for a specific list member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            },
            {
                "name": "note_id",
                "type": "str",
                "required": True,
                "description": "The id for the note."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_list_member_tags",
        "method": "GET",
        "path": "/lists/{list_id}/members/{subscriber_hash}/tags",
        "level": "READONLY",
        "summary": "List member tags",
        "description": "Get the tags on a list member.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address. This endpoint also accepts a list member's email address or contact_id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_list_member_tags",
        "method": "POST",
        "path": "/lists/{list_id}/members/{subscriber_hash}/tags",
        "level": "BASIC",
        "summary": "Add or remove member tags",
        "description": "Add or remove tags from a list member. If a tag that does not exist is passed in and set as 'active', a new tag will be created.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "tags"
        ],
        "body_description": "A list of tags assigned to a list member. Fields: tags, is_syncing."
    },
    {
        "name": "get_lists_id_merge_fields",
        "method": "GET",
        "path": "/lists/{list_id}/merge-fields",
        "level": "READONLY",
        "summary": "List merge fields",
        "description": "Get a list of all merge fields for an audience.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "type",
                "type": "str",
                "required": False,
                "description": "The merge field type."
            },
            {
                "name": "required",
                "type": "bool",
                "required": False,
                "description": "Whether it's a required merge field."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_merge_fields",
        "method": "POST",
        "path": "/lists/{list_id}/merge-fields",
        "level": "BASIC",
        "summary": "Add merge field",
        "description": "Add a new merge field for a specific audience.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name",
            "type"
        ],
        "body_description": "A merge field for an audience. Fields: tag, name, type, required, default_value, public, display_order, options, help_text."
    },
    {
        "name": "get_lists_id_merge_fields_id",
        "method": "GET",
        "path": "/lists/{list_id}/merge-fields/{merge_id}",
        "level": "READONLY",
        "summary": "Get merge field",
        "description": "Get information about a specific merge field.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "merge_id",
                "type": "str",
                "required": True,
                "description": "The id for the merge field."
            }
        ],
        "query_params": [
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_lists_id_merge_fields_id",
        "method": "PATCH",
        "path": "/lists/{list_id}/merge-fields/{merge_id}",
        "level": "ADMIN",
        "summary": "Update merge field",
        "description": "Update a specific merge field.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "merge_id",
                "type": "str",
                "required": True,
                "description": "The id for the merge field."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "A merge field for an audience. Fields: tag, name, required, default_value, public, display_order, options, help_text."
    },
    {
        "name": "delete_lists_id_merge_fields_id",
        "method": "DELETE",
        "path": "/lists/{list_id}/merge-fields/{merge_id}",
        "level": "ADMIN",
        "summary": "Delete merge field",
        "description": "Delete a specific merge field.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "merge_id",
                "type": "str",
                "required": True,
                "description": "The id for the merge field."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "preview_a_segment",
        "method": "GET",
        "path": "/lists/{list_id}/segments",
        "level": "READONLY",
        "summary": "List segments",
        "description": "Get information about all available segments for a specific list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "type",
                "type": "str",
                "required": False,
                "description": "Limit results based on segment type."
            },
            {
                "name": "since_created_at",
                "type": "str",
                "required": False,
                "description": "Restrict results to segments created after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "before_created_at",
                "type": "str",
                "required": False,
                "description": "Restrict results to segments created before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "include_cleaned",
                "type": "bool",
                "required": False,
                "description": "Include cleaned members in response"
            },
            {
                "name": "include_transactional",
                "type": "bool",
                "required": False,
                "description": "Include transactional members in response"
            },
            {
                "name": "include_unsubscribed",
                "type": "bool",
                "required": False,
                "description": "Include unsubscribed members in response"
            },
            {
                "name": "since_updated_at",
                "type": "str",
                "required": False,
                "description": "Restrict results to segments update after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "before_updated_at",
                "type": "str",
                "required": False,
                "description": "Restrict results to segments update before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "exclude_type",
                "type": "str",
                "required": False,
                "description": "Exclude results based on segment type. For example, use `exclude_type=static` to exclude tags from the response.",
                "enum": [
                    "saved",
                    "static",
                    "fuzzy"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_segments",
        "method": "POST",
        "path": "/lists/{list_id}/segments",
        "level": "BASIC",
        "summary": "Add segment",
        "description": "Create a new segment in a specific list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "Information about a specific list segment. Fields: name, static_segment, options."
    },
    {
        "name": "get_lists_id_segments_id",
        "method": "GET",
        "path": "/lists/{list_id}/segments/{segment_id}",
        "level": "READONLY",
        "summary": "Get segment info",
        "description": "Get information about a specific segment.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "segment_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the segment."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "include_cleaned",
                "type": "bool",
                "required": False,
                "description": "Include cleaned members in response"
            },
            {
                "name": "include_transactional",
                "type": "bool",
                "required": False,
                "description": "Include transactional members in response"
            },
            {
                "name": "include_unsubscribed",
                "type": "bool",
                "required": False,
                "description": "Include unsubscribed members in response"
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_segments_id",
        "method": "POST",
        "path": "/lists/{list_id}/segments/{segment_id}",
        "level": "BASIC",
        "summary": "Batch add or remove members",
        "description": "Batch add/remove list members to static segment",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "segment_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the segment."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Members to add/remove to/from a static segment Fields: members_to_add, members_to_remove."
    },
    {
        "name": "patch_lists_id_segments_id",
        "method": "PATCH",
        "path": "/lists/{list_id}/segments/{segment_id}",
        "level": "ADMIN",
        "summary": "Update segment",
        "description": "Update a specific segment in a list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "segment_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the segment."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "Information about a specific list segment. Fields: name, static_segment, options."
    },
    {
        "name": "delete_lists_id_segments_id",
        "method": "DELETE",
        "path": "/lists/{list_id}/segments/{segment_id}",
        "level": "ADMIN",
        "summary": "Delete segment",
        "description": "Delete a specific segment in a list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "segment_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the segment."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_segments_id_members",
        "method": "GET",
        "path": "/lists/{list_id}/segments/{segment_id}/members",
        "level": "READONLY",
        "summary": "List members in segment",
        "description": "Get information about members in a saved segment.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "segment_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the segment."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "include_cleaned",
                "type": "bool",
                "required": False,
                "description": "Include cleaned members in response"
            },
            {
                "name": "include_transactional",
                "type": "bool",
                "required": False,
                "description": "Include transactional members in response"
            },
            {
                "name": "include_unsubscribed",
                "type": "bool",
                "required": False,
                "description": "Include unsubscribed members in response"
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_segments_id_members",
        "method": "POST",
        "path": "/lists/{list_id}/segments/{segment_id}/members",
        "level": "BASIC",
        "summary": "Add member to segment",
        "description": "Add a member to a static segment.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "segment_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the segment."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "email_address"
        ],
        "body_description": "Fields: email_address."
    },
    {
        "name": "delete_lists_id_segments_id_members_id",
        "method": "DELETE",
        "path": "/lists/{list_id}/segments/{segment_id}/members/{subscriber_hash}",
        "level": "ADMIN",
        "summary": "Remove list member from segment",
        "description": "Remove a member from the specified static segment.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "segment_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the segment."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_signup_forms",
        "method": "GET",
        "path": "/lists/{list_id}/signup-forms",
        "level": "READONLY",
        "summary": "List signup forms",
        "description": "Get signup forms for a specific list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_signup_forms",
        "method": "POST",
        "path": "/lists/{list_id}/signup-forms",
        "level": "BASIC",
        "summary": "Customize signup form",
        "description": "Customize a list's default signup form.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "List signup form. Fields: header, contents, styles."
    },
    {
        "name": "get_lists_id_surveys",
        "method": "GET",
        "path": "/lists/{list_id}/surveys",
        "level": "READONLY",
        "summary": "Get information about all surveys for a list",
        "description": "Get information about all available surveys for a specific list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_surveys",
        "method": "POST",
        "path": "/lists/{list_id}/surveys",
        "level": "BASIC",
        "summary": "Create survey",
        "description": "Create a draft survey for an audience.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Survey create request. Fields: title, sections."
    },
    {
        "name": "get_lists_id_surveys_id",
        "method": "GET",
        "path": "/lists/{list_id}/surveys/{survey_id}",
        "level": "READONLY",
        "summary": "Get survey",
        "description": "Get details about a specific survey.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_lists_id_surveys_id",
        "method": "PATCH",
        "path": "/lists/{list_id}/surveys/{survey_id}",
        "level": "ADMIN",
        "summary": "Update survey",
        "description": "Update a survey. When sections is provided, send the complete section list in display order. Any existing section not included is deleted.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Survey update request. Fields: title, is_piped_to_inbox, sections."
    },
    {
        "name": "delete_lists_id_surveys_id",
        "method": "DELETE",
        "path": "/lists/{list_id}/surveys/{survey_id}",
        "level": "ADMIN",
        "summary": "Delete survey",
        "description": "Delete a survey.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_surveys_id_actions_create_email",
        "method": "POST",
        "path": "/lists/{list_id}/surveys/{survey_id}/actions/create-email",
        "level": "BASIC",
        "summary": "Create a Survey Campaign",
        "description": "Utilize the List ID and Survey ID to generate a Campaign that links to your survey.",
        "group": "surveys",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_surveys_id_actions_publish",
        "method": "POST",
        "path": "/lists/{list_id}/surveys/{survey_id}/actions/publish",
        "level": "BASIC",
        "summary": "Publish a Survey",
        "description": "Publish a survey that is in draft, unpublished, or has been previously published and edited.",
        "group": "surveys",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_surveys_id_actions_replicate",
        "method": "POST",
        "path": "/lists/{list_id}/surveys/{survey_id}/actions/replicate",
        "level": "BASIC",
        "summary": "Replicate survey",
        "description": "Replicate a survey.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Survey replicate request. Fields: title, list_id."
    },
    {
        "name": "post_lists_id_surveys_id_actions_unpublish",
        "method": "POST",
        "path": "/lists/{list_id}/surveys/{survey_id}/actions/unpublish",
        "level": "BASIC",
        "summary": "Unpublish a Survey",
        "description": "Unpublish a survey that has been published.",
        "group": "surveys",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "search_tags_by_name",
        "method": "GET",
        "path": "/lists/{list_id}/tag-search",
        "level": "READONLY",
        "summary": "Search for tags on a list by name.",
        "description": "Search for tags on a list by name. If no name is provided, will return all tags on the list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [
            {
                "name": "name",
                "type": "str",
                "required": False,
                "description": "The search query used to filter tags. The search query will be compared to each tag as a prefix, so all tags that have a name starting with this field will be returned."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_lists_id_webhooks",
        "method": "GET",
        "path": "/lists/{list_id}/webhooks",
        "level": "READONLY",
        "summary": "List webhooks",
        "description": "Get information about all webhooks for a specific list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_lists_id_webhooks",
        "method": "POST",
        "path": "/lists/{list_id}/webhooks",
        "level": "BASIC",
        "summary": "Add webhook",
        "description": "Create a new webhook for a specific list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Configure a webhook for the given list. Fields: url, events, sources."
    },
    {
        "name": "get_lists_id_webhooks_id",
        "method": "GET",
        "path": "/lists/{list_id}/webhooks/{webhook_id}",
        "level": "READONLY",
        "summary": "Get webhook info",
        "description": "Get information about a specific webhook.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "webhook_id",
                "type": "str",
                "required": True,
                "description": "The webhook's id."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_lists_id_webhooks_id",
        "method": "PATCH",
        "path": "/lists/{list_id}/webhooks/{webhook_id}",
        "level": "ADMIN",
        "summary": "Update webhook",
        "description": "Update the settings for an existing webhook.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "webhook_id",
                "type": "str",
                "required": True,
                "description": "The webhook's id."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "Configure a webhook for the given list. Fields: url, events, sources."
    },
    {
        "name": "delete_lists_id_webhooks_id",
        "method": "DELETE",
        "path": "/lists/{list_id}/webhooks/{webhook_id}",
        "level": "ADMIN",
        "summary": "Delete webhook",
        "description": "Delete a specific webhook in a list.",
        "group": "lists",
        "path_params": [
            {
                "name": "list_id",
                "type": "str",
                "required": True,
                "description": "The unique ID for the list."
            },
            {
                "name": "webhook_id",
                "type": "str",
                "required": True,
                "description": "The webhook's id."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_ping",
        "method": "GET",
        "path": "/ping",
        "level": "READONLY",
        "summary": "Ping",
        "description": "A health check for the API that won't return any account-specific information.",
        "group": "ping",
        "path_params": [],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_facebook_ads",
        "method": "GET",
        "path": "/reporting/facebook-ads",
        "level": "READONLY",
        "summary": "List facebook ads reports",
        "description": "Get reports of Facebook ads.",
        "group": "reporting",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "created_at",
                    "updated_at",
                    "end_time"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_facebook_ads_id",
        "method": "GET",
        "path": "/reporting/facebook-ads/{outreach_id}",
        "level": "READONLY",
        "summary": "Get facebook ad report",
        "description": "Get report of a Facebook ad.",
        "group": "reporting",
        "path_params": [
            {
                "name": "outreach_id",
                "type": "str",
                "required": True,
                "description": "The outreach id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_facebook_ads_id_ecommerce_product_activity",
        "method": "GET",
        "path": "/reporting/facebook-ads/{outreach_id}/ecommerce-product-activity",
        "level": "READONLY",
        "summary": "List facebook ecommerce report",
        "description": "Get breakdown of product activity for an outreach.",
        "group": "reporting",
        "path_params": [
            {
                "name": "outreach_id",
                "type": "str",
                "required": True,
                "description": "The outreach id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "title",
                    "total_revenue",
                    "total_purchased"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_landing_pages",
        "method": "GET",
        "path": "/reporting/landing-pages",
        "level": "READONLY",
        "summary": "List landing pages reports",
        "description": "Get reports of landing pages.",
        "group": "reporting",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_landing_pages_id",
        "method": "GET",
        "path": "/reporting/landing-pages/{outreach_id}",
        "level": "READONLY",
        "summary": "Get landing page report",
        "description": "Get report of a landing page.",
        "group": "reporting",
        "path_params": [
            {
                "name": "outreach_id",
                "type": "str",
                "required": True,
                "description": "The outreach id."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_surveys",
        "method": "GET",
        "path": "/reporting/surveys",
        "level": "READONLY",
        "summary": "List survey reports",
        "description": "Get reports for surveys.",
        "group": "reporting",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_surveys_id",
        "method": "GET",
        "path": "/reporting/surveys/{survey_id}",
        "level": "READONLY",
        "summary": "Get survey report",
        "description": "Get report for a survey.",
        "group": "reporting",
        "path_params": [
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_surveys_id_questions",
        "method": "GET",
        "path": "/reporting/surveys/{survey_id}/questions",
        "level": "READONLY",
        "summary": "List survey question reports",
        "description": "Get reports for survey questions.",
        "group": "reporting",
        "path_params": [
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_surveys_id_questions_id",
        "method": "GET",
        "path": "/reporting/surveys/{survey_id}/questions/{question_id}",
        "level": "READONLY",
        "summary": "Get survey question report",
        "description": "Get report for a survey question.",
        "group": "reporting",
        "path_params": [
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            },
            {
                "name": "question_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey question."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_surveys_id_questions_id_answers",
        "method": "GET",
        "path": "/reporting/surveys/{survey_id}/questions/{question_id}/answers",
        "level": "READONLY",
        "summary": "List answers for question",
        "description": "Get answers for a survey question.",
        "group": "reporting",
        "path_params": [
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            },
            {
                "name": "question_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey question."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "respondent_familiarity_is",
                "type": "str",
                "required": False,
                "description": "Filter survey responses by familiarity of the respondents.",
                "enum": [
                    "new",
                    "known",
                    "unknown"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_surveys_id_responses",
        "method": "GET",
        "path": "/reporting/surveys/{survey_id}/responses",
        "level": "READONLY",
        "summary": "List survey responses",
        "description": "Get responses to a survey.",
        "group": "reporting",
        "path_params": [
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "answered_question",
                "type": "int",
                "required": False,
                "description": "The ID of the question that was answered."
            },
            {
                "name": "chose_answer",
                "type": "str",
                "required": False,
                "description": "The ID of the option chosen to filter responses on."
            },
            {
                "name": "respondent_familiarity_is",
                "type": "str",
                "required": False,
                "description": "Filter survey responses by familiarity of the respondents.",
                "enum": [
                    "new",
                    "known",
                    "unknown"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reporting_surveys_id_responses_id",
        "method": "GET",
        "path": "/reporting/surveys/{survey_id}/responses/{response_id}",
        "level": "READONLY",
        "summary": "Get survey response",
        "description": "Get a single survey response.",
        "group": "reporting",
        "path_params": [
            {
                "name": "survey_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey."
            },
            {
                "name": "response_id",
                "type": "str",
                "required": True,
                "description": "The ID of the survey response."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports",
        "method": "GET",
        "path": "/reports",
        "level": "READONLY",
        "summary": "List campaign reports",
        "description": "Get campaign reports.",
        "group": "reports",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "type",
                "type": "str",
                "required": False,
                "description": "The campaign type.",
                "enum": [
                    "regular",
                    "plaintext",
                    "absplit",
                    "rss",
                    "variate"
                ]
            },
            {
                "name": "before_send_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to campaigns sent before the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "since_send_time",
                "type": "str",
                "required": False,
                "description": "Restrict the response to campaigns sent after the set time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id",
        "method": "GET",
        "path": "/reports/{campaign_id}",
        "level": "READONLY",
        "summary": "Get campaign report",
        "description": "Get report details for a specific sent campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_abuse_reports_id",
        "method": "GET",
        "path": "/reports/{campaign_id}/abuse-reports",
        "level": "READONLY",
        "summary": "List abuse reports",
        "description": "Get a list of abuse complaints for a specific campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_abuse_reports_id_id",
        "method": "GET",
        "path": "/reports/{campaign_id}/abuse-reports/{report_id}",
        "level": "READONLY",
        "summary": "Get abuse report",
        "description": "Get information about a specific abuse report for a campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "report_id",
                "type": "str",
                "required": True,
                "description": "The id for the abuse report."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_advice",
        "method": "GET",
        "path": "/reports/{campaign_id}/advice",
        "level": "READONLY",
        "summary": "List campaign feedback",
        "description": "Get feedback based on a campaign's statistics. Advice feedback is based on campaign stats like opens, clicks, unsubscribes, bounces, and more.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_click_details",
        "method": "GET",
        "path": "/reports/{campaign_id}/click-details",
        "level": "READONLY",
        "summary": "List campaign details",
        "description": "Get information about clicks on specific links in your Mailchimp campaigns.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns click reports sorted by the specified field.",
                "enum": [
                    "total_clicks",
                    "unique_clicks"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            },
            {
                "name": "filter_bots",
                "type": "bool",
                "required": False,
                "description": "When True, exclude automated bot clicks so the returned click counts reflect human clicks only, matching the in-app Recipient Activity view. Filtering changes a link's counts, but never removes a link from the…",
                "default": False
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_click_details_id",
        "method": "GET",
        "path": "/reports/{campaign_id}/click-details/{link_id}",
        "level": "READONLY",
        "summary": "Get campaign link details",
        "description": "Get click details for a specific link in a campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "link_id",
                "type": "str",
                "required": True,
                "description": "The id for the link."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "filter_bots",
                "type": "bool",
                "required": False,
                "description": "When True, exclude automated bot clicks so the returned click counts reflect human clicks only, matching the in-app Recipient Activity view. Filtering changes a link's counts, but never removes a link from the…",
                "default": False
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_click_details_id_members",
        "method": "GET",
        "path": "/reports/{campaign_id}/click-details/{link_id}/members",
        "level": "READONLY",
        "summary": "List clicked link subscribers",
        "description": "Get information about list members who clicked on a specific link in a campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "link_id",
                "type": "str",
                "required": True,
                "description": "The id for the link."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_click_details_id_members_id",
        "method": "GET",
        "path": "/reports/{campaign_id}/click-details/{link_id}/members/{subscriber_hash}",
        "level": "READONLY",
        "summary": "Get clicked link subscriber",
        "description": "Get information about a specific subscriber who clicked a link in a specific campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "link_id",
                "type": "str",
                "required": True,
                "description": "The id for the link."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_domain_performance",
        "method": "GET",
        "path": "/reports/{campaign_id}/domain-performance",
        "level": "READONLY",
        "summary": "List domain performance stats",
        "description": "Get statistics for the top-performing email domains in a campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_ecommerce_product_activity",
        "method": "GET",
        "path": "/reports/{campaign_id}/ecommerce-product-activity",
        "level": "READONLY",
        "summary": "List campaign product activity",
        "description": "Get breakdown of product activity for a campaign",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns files sorted by the specified field.",
                "enum": [
                    "title",
                    "total_revenue",
                    "total_purchased"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_eepurl",
        "method": "GET",
        "path": "/reports/{campaign_id}/eepurl",
        "level": "READONLY",
        "summary": "List EepURL activity",
        "description": "Get a summary of social activity for the campaign, tracked by EepURL.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_email_activity",
        "method": "GET",
        "path": "/reports/{campaign_id}/email-activity",
        "level": "READONLY",
        "summary": "List email activity",
        "description": "Get a list of member's subscriber activity in a specific campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "since",
                "type": "str",
                "required": False,
                "description": "Restrict results to email activity events that occur after a specific time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "filter_bots",
                "type": "bool",
                "required": False,
                "description": "When True, exclude automated bot and Apple Mail Privacy Protection (MPP) proxy activity so the returned activity reflects human-only opens and clicks, matching the in-app Recipient Activity view. Filtering removes…",
                "default": False
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_email_activity_id",
        "method": "GET",
        "path": "/reports/{campaign_id}/email-activity/{subscriber_hash}",
        "level": "READONLY",
        "summary": "Get subscriber email activity",
        "description": "Get a specific list member's activity in a campaign including opens, clicks, and bounces.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "since",
                "type": "str",
                "required": False,
                "description": "Restrict results to email activity events that occur after a specific time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "filter_bots",
                "type": "bool",
                "required": False,
                "description": "When True, exclude automated bot and Apple Mail Privacy Protection (MPP) proxy activity so the returned activity reflects human-only opens and clicks, matching the in-app Recipient Activity view. Filtering removes…",
                "default": False
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_locations",
        "method": "GET",
        "path": "/reports/{campaign_id}/locations",
        "level": "READONLY",
        "summary": "List top open activities",
        "description": "Get top open locations for a specific campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_open_details",
        "method": "GET",
        "path": "/reports/{campaign_id}/open-details",
        "level": "READONLY",
        "summary": "List campaign open details",
        "description": "Get detailed information about any campaign emails that were opened by a list member.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "since",
                "type": "str",
                "required": False,
                "description": "Restrict results to campaign open events that occur after a specific time. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns open reports sorted by the specified field.",
                "enum": [
                    "opens_count"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            },
            {
                "name": "filter_bots",
                "type": "bool",
                "required": False,
                "description": "When True, exclude automated (proxy/bot) opens so the returned open counts reflect human opens only, matching the in-app Recipient Activity view. A member whose opens are all automated is excluded from the human-only…",
                "default": False
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_open_details_id_members_id",
        "method": "GET",
        "path": "/reports/{campaign_id}/open-details/{subscriber_hash}",
        "level": "READONLY",
        "summary": "Get opened campaign subscriber",
        "description": "Get information about a specific subscriber who opened a campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "filter_bots",
                "type": "bool",
                "required": False,
                "description": "When True, exclude automated (proxy/bot) opens so the returned open counts reflect human opens only, matching the in-app Recipient Activity view. A member whose opens are all automated is excluded from the human-only…",
                "default": False
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_sent_to",
        "method": "GET",
        "path": "/reports/{campaign_id}/sent-to",
        "level": "READONLY",
        "summary": "List campaign recipients",
        "description": "Get information about campaign recipients.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_sent_to_id",
        "method": "GET",
        "path": "/reports/{campaign_id}/sent-to/{subscriber_hash}",
        "level": "READONLY",
        "summary": "Get campaign recipient info",
        "description": "Get information about a specific campaign recipient.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_sub_reports_id",
        "method": "GET",
        "path": "/reports/{campaign_id}/sub-reports",
        "level": "READONLY",
        "summary": "List child campaign reports",
        "description": "Get a list of reports with child campaigns for a specific parent campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_unsubscribed",
        "method": "GET",
        "path": "/reports/{campaign_id}/unsubscribed",
        "level": "READONLY",
        "summary": "List unsubscribed members",
        "description": "Get information about members who have unsubscribed from a specific campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_reports_id_unsubscribed_id",
        "method": "GET",
        "path": "/reports/{campaign_id}/unsubscribed/{subscriber_hash}",
        "level": "READONLY",
        "summary": "Get unsubscribed member",
        "description": "Get information about a specific list member who unsubscribed from a campaign.",
        "group": "reports",
        "path_params": [
            {
                "name": "campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the campaign."
            },
            {
                "name": "subscriber_hash",
                "type": "str",
                "required": True,
                "description": "The MD5 hash of the lowercase version of the list member's email address."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_search_campaigns",
        "method": "GET",
        "path": "/search-campaigns",
        "level": "READONLY",
        "summary": "Search campaigns",
        "description": "Search all campaigns for the specified query terms.",
        "group": "search_campaigns",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "query",
                "type": "str",
                "required": True,
                "description": "The search query used to filter results."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_search_members",
        "method": "GET",
        "path": "/search-members",
        "level": "READONLY",
        "summary": "Search members",
        "description": "Search for list members. This search can be restricted to a specific list, or can be used to search across all lists in an account.",
        "group": "search_members",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "query",
                "type": "str",
                "required": True,
                "description": "The search query used to filter results. Query should be a valid email, or a string representing a contact's first or last name."
            },
            {
                "name": "list_id",
                "type": "str",
                "required": False,
                "description": "The unique id for the list."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_sms_campaigns",
        "method": "GET",
        "path": "/sms-campaigns",
        "level": "READONLY",
        "summary": "List SMS campaigns",
        "description": "Get all SMS campaigns in an account.",
        "group": "sms-campaigns",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_sms_campaigns",
        "method": "POST",
        "path": "/sms-campaigns",
        "level": "BASIC",
        "summary": "Add SMS campaign",
        "description": "Create a new SMS campaign.",
        "group": "sms-campaigns",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "The settings for creating a new SMS campaign. Fields: name, list_id, folder_id, segments, excluded_segments."
    },
    {
        "name": "get_sms_campaigns_id",
        "method": "GET",
        "path": "/sms-campaigns/{sms_campaign_id}",
        "level": "READONLY",
        "summary": "Get SMS campaign info",
        "description": "Get information about a specific SMS campaign.",
        "group": "sms-campaigns",
        "path_params": [
            {
                "name": "sms_campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the SMS campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_sms_campaigns_id",
        "method": "PATCH",
        "path": "/sms-campaigns/{sms_campaign_id}",
        "level": "ADMIN",
        "summary": "Update SMS campaign settings",
        "description": "Update some or all of the settings for a specific SMS campaign.",
        "group": "sms-campaigns",
        "path_params": [
            {
                "name": "sms_campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the SMS campaign."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [],
        "body_description": "The settings for updating an SMS campaign. Fields: name, folder_id, segments, excluded_segments."
    },
    {
        "name": "delete_sms_campaigns_id",
        "method": "DELETE",
        "path": "/sms-campaigns/{sms_campaign_id}",
        "level": "ADMIN",
        "summary": "Delete SMS campaign",
        "description": "Remove an SMS campaign from your Mailchimp account.",
        "group": "sms-campaigns",
        "path_params": [
            {
                "name": "sms_campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the SMS campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_sms_campaigns_id_actions_cancel_send",
        "method": "POST",
        "path": "/sms-campaigns/{sms_campaign_id}/actions/cancel-send",
        "level": "BASIC",
        "summary": "Cancel SMS campaign send",
        "description": "Cancel a scheduled or sending SMS campaign.",
        "group": "sms-campaigns",
        "path_params": [
            {
                "name": "sms_campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the SMS campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_sms_campaigns_id_actions_schedule",
        "method": "POST",
        "path": "/sms-campaigns/{sms_campaign_id}/actions/schedule",
        "level": "BASIC",
        "summary": "Schedule SMS campaign",
        "description": "Schedule an SMS campaign to send at a specific time.",
        "group": "sms-campaigns",
        "path_params": [
            {
                "name": "sms_campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the SMS campaign."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "schedule_time"
        ],
        "body_description": "Fields: schedule_time."
    },
    {
        "name": "post_sms_campaigns_id_actions_send",
        "method": "POST",
        "path": "/sms-campaigns/{sms_campaign_id}/actions/send",
        "level": "BASIC",
        "summary": "Send SMS campaign",
        "description": "Send an SMS campaign.",
        "group": "sms-campaigns",
        "path_params": [
            {
                "name": "sms_campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the SMS campaign."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_sms_campaigns_id_content",
        "method": "GET",
        "path": "/sms-campaigns/{sms_campaign_id}/content",
        "level": "READONLY",
        "summary": "Get SMS campaign content",
        "description": "Get the content for an SMS campaign.",
        "group": "sms-campaigns",
        "path_params": [
            {
                "name": "sms_campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the SMS campaign."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "put_sms_campaigns_id_content",
        "method": "PUT",
        "path": "/sms-campaigns/{sms_campaign_id}/content",
        "level": "ADMIN",
        "summary": "Set SMS campaign content",
        "description": "Set the content for an SMS campaign.",
        "group": "sms-campaigns",
        "path_params": [
            {
                "name": "sms_campaign_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the SMS campaign."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "message_body"
        ],
        "body_description": "The settings for setting the content of an SMS campaign. Fields: message_body, media."
    },
    {
        "name": "get_template_folders",
        "method": "GET",
        "path": "/template-folders",
        "level": "READONLY",
        "summary": "List template folders",
        "description": "Get all folders used to organize templates.",
        "group": "template_folders",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_template_folders",
        "method": "POST",
        "path": "/template-folders",
        "level": "BASIC",
        "summary": "Add template folder",
        "description": "Create a new template folder.",
        "group": "template_folders",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "A folder used to organize templates. Fields: name."
    },
    {
        "name": "get_template_folders_id",
        "method": "GET",
        "path": "/template-folders/{folder_id}",
        "level": "READONLY",
        "summary": "Get template folder",
        "description": "Get information about a specific folder used to organize templates.",
        "group": "template_folders",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the template folder."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_template_folders_id",
        "method": "PATCH",
        "path": "/template-folders/{folder_id}",
        "level": "ADMIN",
        "summary": "Update template folder",
        "description": "Update a specific folder used to organize templates.",
        "group": "template_folders",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the template folder."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name"
        ],
        "body_description": "A folder used to organize templates. Fields: name."
    },
    {
        "name": "delete_template_folders_id",
        "method": "DELETE",
        "path": "/template-folders/{folder_id}",
        "level": "ADMIN",
        "summary": "Delete template folder",
        "description": "Delete a specific template folder, and mark all the templates in the folder as 'unfiled'.",
        "group": "template_folders",
        "path_params": [
            {
                "name": "folder_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the template folder."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_templates",
        "method": "GET",
        "path": "/templates",
        "level": "READONLY",
        "summary": "List templates",
        "description": "Get a list of an account's available templates.",
        "group": "templates",
        "path_params": [],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "count",
                "type": "int",
                "required": False,
                "description": "The number of records to return. Default value is 10. Maximum value is 1000",
                "default": 10
            },
            {
                "name": "offset",
                "type": "int",
                "required": False,
                "description": "Used for pagination, this is the number of records from a collection to skip. Default value is 0.",
                "default": 0
            },
            {
                "name": "created_by",
                "type": "str",
                "required": False,
                "description": "The Mailchimp account user who created the template."
            },
            {
                "name": "since_date_created",
                "type": "str",
                "required": False,
                "description": "Restrict the response to templates created after the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "before_date_created",
                "type": "str",
                "required": False,
                "description": "Restrict the response to templates created before the set date. Uses ISO 8601 time format: 2015-10-21T15:41:36+00:00."
            },
            {
                "name": "type",
                "type": "str",
                "required": False,
                "description": "Limit results based on template type."
            },
            {
                "name": "category",
                "type": "str",
                "required": False,
                "description": "Limit results based on category."
            },
            {
                "name": "folder_id",
                "type": "str",
                "required": False,
                "description": "The unique folder id."
            },
            {
                "name": "sort_field",
                "type": "str",
                "required": False,
                "description": "Returns user templates sorted by the specified field.",
                "enum": [
                    "date_created",
                    "date_edited",
                    "name"
                ]
            },
            {
                "name": "content_type",
                "type": "str",
                "required": False,
                "description": "Limit results based on how the template's content is put together. Only templates of type `user` can be filtered by `content_type`. If you want to retrieve saved templates created with the legacy email editor, then…",
                "enum": [
                    "html",
                    "template",
                    "multichannel"
                ]
            },
            {
                "name": "sort_dir",
                "type": "str",
                "required": False,
                "description": "Determines the order direction for sorted results.",
                "enum": [
                    "ASC",
                    "DESC"
                ]
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "post_templates",
        "method": "POST",
        "path": "/templates",
        "level": "BASIC",
        "summary": "Add template",
        "description": "Create a new template for the account. Only Classic templates are supported.",
        "group": "templates",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name",
            "html"
        ],
        "body_description": "Information about a specific template. Fields: name, folder_id, html."
    },
    {
        "name": "get_templates_id",
        "method": "GET",
        "path": "/templates/{template_id}",
        "level": "READONLY",
        "summary": "Get template info",
        "description": "Get information about a specific template.",
        "group": "templates",
        "path_params": [
            {
                "name": "template_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the template."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "patch_templates_id",
        "method": "PATCH",
        "path": "/templates/{template_id}",
        "level": "ADMIN",
        "summary": "Update template",
        "description": "Update the name, HTML, or `folder_id` of an existing template.",
        "group": "templates",
        "path_params": [
            {
                "name": "template_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the template."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "name",
            "html"
        ],
        "body_description": "Information about a specific template. Fields: name, folder_id, html."
    },
    {
        "name": "delete_templates_id",
        "method": "DELETE",
        "path": "/templates/{template_id}",
        "level": "ADMIN",
        "summary": "Delete template",
        "description": "Delete a specific template.",
        "group": "templates",
        "path_params": [
            {
                "name": "template_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the template."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_templates_id_default_content",
        "method": "GET",
        "path": "/templates/{template_id}/default-content",
        "level": "READONLY",
        "summary": "View default content",
        "description": "Get the sections that you can edit in a template, including each section's default content.",
        "group": "templates",
        "path_params": [
            {
                "name": "template_id",
                "type": "str",
                "required": True,
                "description": "The unique id for the template."
            }
        ],
        "query_params": [
            {
                "name": "fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to return. Reference parameters of sub-objects with dot notation."
            },
            {
                "name": "exclude_fields",
                "type": "str",
                "required": False,
                "description": "A comma-separated list of fields to exclude. Reference parameters of sub-objects with dot notation."
            }
        ],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "get_verified_domains",
        "method": "GET",
        "path": "/verified-domains",
        "level": "READONLY",
        "summary": "List sending domains",
        "description": "Get all of the sending domains on the account.",
        "group": "verified_domains",
        "path_params": [],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "create_verified_domain",
        "method": "POST",
        "path": "/verified-domains",
        "level": "BASIC",
        "summary": "Add domain to account",
        "description": "Add a domain to the account.",
        "group": "verified_domains",
        "path_params": [],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "verification_email"
        ],
        "body_description": "The verified domains currently on the account. Fields: verification_email."
    },
    {
        "name": "get_verified_domain",
        "method": "GET",
        "path": "/verified-domains/{domain_name}",
        "level": "READONLY",
        "summary": "Get domain info",
        "description": "Get the details for a single domain on the account.",
        "group": "verified_domains",
        "path_params": [
            {
                "name": "domain_name",
                "type": "str",
                "required": True,
                "description": "The domain name."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "delete_verified_domain",
        "method": "DELETE",
        "path": "/verified-domains/{domain_name}",
        "level": "ADMIN",
        "summary": "Delete domain",
        "description": "Delete a verified domain from the account.",
        "group": "verified_domains",
        "path_params": [
            {
                "name": "domain_name",
                "type": "str",
                "required": True,
                "description": "The domain name."
            }
        ],
        "query_params": [],
        "has_body": False,
        "body_required": [],
        "body_description": ""
    },
    {
        "name": "verify_domain",
        "method": "POST",
        "path": "/verified-domains/{domain_name}/actions/verify",
        "level": "BASIC",
        "summary": "Verify domain",
        "description": "Verify a domain for sending.",
        "group": "verified_domains",
        "path_params": [
            {
                "name": "domain_name",
                "type": "str",
                "required": True,
                "description": "The domain name."
            }
        ],
        "query_params": [],
        "has_body": True,
        "body_required": [
            "code"
        ],
        "body_description": "Submit a response to the verification challenge and verify a domain for sending. Fields: code."
    }
]


#: Operation lookup by tool name.
BY_NAME: dict[str, dict[str, Any]] = {op["name"]: op for op in OPERATIONS}

#: Distinct API groups (Mailchimp's own spec tags), for optional filtering.
GROUPS: tuple[str, ...] = tuple(sorted({op["group"] for op in OPERATIONS}))
