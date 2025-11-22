from gui.gui_gradio import ShortGptUI

# Apply Gradio-Pydantic compatibility patch
try:
    from fix_gradio_compatibility import patch_gradio_client
    patch_gradio_client()
except Exception as e:
    print(f"⚠️  Warning: Could not apply Gradio compatibility patch: {e}")
    print("   The application may encounter errors during startup.")

app = ShortGptUI(colab=False)
app.launch()