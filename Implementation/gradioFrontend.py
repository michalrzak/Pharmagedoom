import gradio as gr
import pandas as pd
import backend

test_data = pd.DataFrame([["a", "b", "c", "a", "b", "c"], ["d", "e", "f", "a", "b", "c"]],
                         columns=["A", "B", "C", "a", "b", "c"])
medication_data = backend.MedicationData()


def get_warning_message(n_warning: int):
    return f"### ⚠️ {n_warning} Warnings found"


def get_error_message(n_export: int):
    return f"### ⛔ {n_export} Errors found"


def add_medication(medication_name: str, manufacturer_name: str) -> pd.DataFrame:
    medication_data.add_new_medication(medication_name, manufacturer_name)
    # backend.get_warnings()
    # backend.get_errors()
    #return medication_data.get_medication_data()
    return {
		medication_list: test_data,
		warnings_label: get_warning_message(len(test_data)),
		warnings_list: test_data,
		error_lable: get_error_message(len(test_data)),
		error_list: test_data
	}


def export_list():
    #medication_data.export_file("some.csv")
    test_data.to_csv("some.csv")


def import_list():
    #return medication_data.import_file(filepath="some.csv")
    return {
        app_column: gr.update(visible=False),
        file_upload_column: gr.update(visible=True)
    }


def export_list_():
    # backend call
    # output = backend.MedicationData.get_medication_data()
    output = test_data
    test_data.to_csv("output.csv")
    return {
        app_column: gr.update(visible=False),
        file_download_column: gr.update(visible=True),
        dowload_file: "output.csv"
    }


def upload_file_process(file):
    with file as temp:
        dataFrame = pd.read_csv(temp.name)
    return {
        app_column: gr.update(visible=True),
        file_upload_column: gr.update(visible=False),
        medication_list: dataFrame
    }


def finished_download():
    return {
        app_column: gr.update(visible=True),
        file_download_column: gr.update(visible=False)
    }


with gr.Blocks() as demo:
    with gr.Column(visible=False) as file_upload_column:
        upload_file = gr.File(file_types=[".csv"])
        upload_button = gr.Button("Upload")

    with gr.Column(visible=False) as file_download_column:
        dowload_file = gr.File(file_types=[".csv"], interactive=False)
        dowload_button = gr.Button("finnished")

    with gr.Column(visible=True) as app_column:
        with gr.Row():
            with gr.Column(scale=20):
                medication_label = gr.Markdown("### Medication list")
                medication_list = gr.Dataframe(test_data)
            with gr.Column(scale=2):
                medication_name = gr.Textbox(label="Medication")
                manufacturer_name = gr.Textbox(label="Manufacturer")

                with gr.Row():
                    import_button = gr.Button("Import List")
                    import_button.style(size="lg", full_width=False)
                    import_button.click(fn=import_list, outputs=[app_column, file_upload_column])
                    export_button = gr.Button("Export List")
                    export_button.style(size="lg", full_width=False)
                    export_button.click(fn=export_list, outputs=[app_column, file_download_column, dowload_file])

            with gr.Column(scale=1):
                submit = gr.Button("➕")
                submit.style(size="lg", full_width=False)

        with gr.Row():
            with gr.Column():
                warnings_label = gr.Markdown(get_warning_message(0))
                warnings_list = gr.Dataframe(test_data)

            with gr.Column():
                error_lable = gr.Markdown(get_error_message(9))
                error_list = gr.Dataframe(test_data)

    # has to be deffined here as it modiefies elements from the app_column
    upload_button.click(fn=upload_file_process, inputs=upload_file,
                        outputs=[app_column, file_upload_column, medication_list])

    dowload_button.click(fn=finished_download, outputs=[app_column, file_download_column])

    submit.click(fn=add_medication, inputs=[medication_name, manufacturer_name],
                 outputs=[medication_list,
                          warnings_label, warnings_list,
                          error_lable, error_list],
                 api_name="add_medication")
