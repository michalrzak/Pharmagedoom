# Pharmagedoom

Another applicaton for checking drug-drug-interaction.

This project was created for the course "Medizinische Entscheidungsunterstützung" (Medical decission support) of the Medical University of Vienna ([course link](https://campus.meduniwien.ac.at/med.campus/ee/ui/ca2/app/desktop/#/slc.tm.cp/student/courses/355577?$ctx=design=ca;lang=de&$scrollTo=toc_overview)).

## Mock-up
We have created a design-mock up of the app. In this mock-up a user can:
1. add new medications to the medication list
2. view any interaction these medications may have. For this we have deffined both a warning and an error level, depending on the severity of the interaction
3. import and export the current list, to be able to save and load the lists

![MOCK-UP](https://github.com/michalrzak/unnamed_DDI_project/blob/main/Pharmaggedoom_MockUp.png)

## Implementation
- The implementation of the app was done useing `python3.11` and gradio for the frontend. 
- Install the requirements inside a `python3.11` virtual environment via `pip install -r requirements.txt`.
- Run the app by navigating into the `Implementation` directory and running `gradio gradioFrontend.py`.

The interface of our implementation was design to closely resamble the mock up interface.
![IMPLEMNTATION](https://github.com/michalrzak/unnamed_DDI_project/blob/main/Pharmaggedoom_Interface.png)

### Notes about implementation
- As this is only a prototype implementation some corners were cut. If you want to test the drug-drug-interaction, you have to use the drugs defined in [our dataset](https://github.com/michalrzak/unnamed_DDI_project/blob/main/Implementation/DataConversion/trimmed_data.csv). 
- There is no back button from the `Import list`
