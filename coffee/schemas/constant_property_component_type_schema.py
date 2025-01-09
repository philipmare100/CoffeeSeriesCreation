from coffee.schemas.base_schema import with_base_properties


@with_base_properties
def get_constant_property_component_type_schema():
    """JSON:API schema for constant property. Used for all CRUD operations."""
    return {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "id": "string",
        "properties": {
            "component_type_id": {
                "type": ["string", "null"]
            },
            "component_type": {
                "relation": "to-one",
                "resource": ["component_type"],
                "description": "Detailed relationship representation to Component Type."
            },
            "constant_property_id": {
                "type": ["string", "null"]
            },
            "constant_property": {
                "relation": "to-one",
                "resource": ["constant_property"],
                "description": "Detailed relationship representation to Constant Property."
            },
            "unique_values": {
                "type": "boolean",
                "default": False
            },
            "is_closed": {
                "type": "boolean",
                "default": False
            },
            "low": {
                "type": ["number", "null"]
            },
            "lowlow": {
                "type": ["number", "null"]
            },
            "hi": {
                "type": ["number", "null"]
            },
            "hihi": {
                "type": ["number", "null"]
            }
        },
        "required": ["component_type_id", "constant_property_id"],
        "additionalProperties": True,
        "description": "Mapping between Constant Property and Component Type, ensuring a unique constraint on "
                       "component type and constant property."
    }
