#!/usr/bin/env python3
"""
Test script to verify Gradio-Pydantic compatibility fix

This script tests whether the compatibility fixes are working by:
1. Checking Pydantic version
2. Testing the gradio_client patch
3. Attempting to create a simple Gradio interface
"""

import sys

def test_pydantic_version():
    """Test that Pydantic version is compatible"""
    print("🔍 Testing Pydantic version...")
    try:
        import pydantic
        version = pydantic.VERSION
        major, minor = int(version.split('.')[0]), int(version.split('.')[1])

        if major == 2 and minor >= 11:
            print(f"❌ Pydantic version {version} is incompatible (needs < 2.11.0)")
            return False
        else:
            print(f"✅ Pydantic version {version} is compatible")
            return True
    except Exception as e:
        print(f"❌ Error checking Pydantic: {e}")
        return False


def test_gradio_patch():
    """Test that the Gradio compatibility patch works"""
    print("\n🔍 Testing Gradio compatibility patch...")
    try:
        from fix_gradio_compatibility import patch_gradio_client
        success = patch_gradio_client()
        if success:
            print("✅ Gradio patch applied successfully")
            return True
        else:
            print("⚠️  Patch not applied (may not be needed)")
            return True  # Still OK if patch isn't needed
    except Exception as e:
        print(f"❌ Error applying patch: {e}")
        return False


def test_gradio_import():
    """Test that Gradio can be imported and basic functionality works"""
    print("\n🔍 Testing Gradio import and basic functionality...")
    try:
        import gradio as gr
        print(f"✅ Gradio {gr.__version__} imported successfully")

        # Try creating a simple interface
        def dummy_func(x):
            return x

        demo = gr.Interface(fn=dummy_func, inputs="text", outputs="text")
        print("✅ Created test Gradio interface successfully")

        # Try getting API info (this is where the error occurs)
        try:
            api_info = demo.get_api_info()
            print("✅ API info generation successful")
            return True
        except TypeError as e:
            if "bool" in str(e) and "not iterable" in str(e):
                print(f"❌ API info generation failed with compatibility error: {e}")
                return False
            raise

    except Exception as e:
        print(f"❌ Error with Gradio: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_shortgpt_imports():
    """Test that ShortGPT modules can be imported"""
    print("\n🔍 Testing ShortGPT imports...")
    try:
        from gui.gui_gradio import ShortGptUI
        print("✅ ShortGPT GUI imported successfully")
        return True
    except Exception as e:
        print(f"❌ Error importing ShortGPT: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("ShortGPT Compatibility Test Suite")
    print("=" * 60)

    results = {
        "Pydantic Version": test_pydantic_version(),
        "Gradio Patch": test_gradio_patch(),
        "Gradio Import": test_gradio_import(),
        "ShortGPT Imports": test_shortgpt_imports()
    }

    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)

    all_passed = True
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test_name:<25} {status}")
        if not passed:
            all_passed = False

    print("=" * 60)

    if all_passed:
        print("\n🎉 All tests passed! ShortGPT should launch successfully.")
        print("\nTo run ShortGPT:")
        print("  ./run_mac.sh")
        print("\nOr manually:")
        print("  source venv/bin/activate")
        print("  python runShortGPT.py")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        print("\nTry reinstalling dependencies:")
        print('  pip install "pydantic>=2.0.0,<2.11.0" --force-reinstall')
        return 1


if __name__ == "__main__":
    sys.exit(main())
