#!/usr/bin/env python3
"""
Gradio-Pydantic Compatibility Fix for ShortGPT

This script patches the gradio_client.utils module to handle boolean
schema values properly, fixing the "TypeError: argument of type 'bool'
is not iterable" error.

This is a temporary workaround for the known Gradio-Pydantic compatibility
issue: https://github.com/gradio-app/gradio/issues/11722
"""

import sys


def patch_gradio_client():
    """Monkey patch gradio_client.utils.get_type to handle boolean schemas."""
    try:
        import gradio_client.utils as utils

        # Store the original function
        original_get_type = utils.get_type

        def patched_get_type(schema):
            """Patched get_type that handles boolean schemas."""
            # Handle boolean schema values
            if isinstance(schema, bool):
                return "boolean" if schema else "any"

            # Call the original function for all other cases
            return original_get_type(schema)

        # Apply the patch
        utils.get_type = patched_get_type
        print("✅ Successfully patched gradio_client.utils.get_type")
        return True

    except ImportError:
        print("⚠️  gradio_client not found. Patch not applied.")
        return False
    except Exception as e:
        print(f"❌ Error applying patch: {e}")
        return False


if __name__ == "__main__":
    # Run the patch
    success = patch_gradio_client()
    sys.exit(0 if success else 1)
