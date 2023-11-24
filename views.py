from django.shortcuts import render
from joblib import load
import numpy as np

model = load('./savedmodels/RF_DIA_9.3.joblib')


def predictor(request):
    if request.method == 'POST':
        Mean_Pulse_Width_at_Half_Height = float(request.POST['Mean_Pulse_Width_at_Half_Height'])
        Mean_Peak_to_Peak_Interval = float(request.POST['Mean_Peak_to_Peak_Interval'])
        Mean_Pulse_Interval = float(request.POST['Mean_Pulse_Interval'])
        Mean_Peak_Values_PPG_2 = float(request.POST['Mean_Peak_Values_PPG_2'])
        Mean_Offset_Values_PPG_2 = float(request.POST['Mean_Offset_Values_PPG_2'])
        Mean_Peak_Time_Interval_of_PPG_2 = float(request.POST['Mean_Peak_Time_Interval_of_PPG_2'])
        Mean_Offset_Time_Interval_of_PPG_2 = float(request.POST['Mean_Offset_Time_Interval_of_PPG_2'])
        Mean_Systolic_Peak_Time = float(request.POST['Mean_Systolic_Peak_Time'])
        Mean_Peak_Amplitude = float(request.POST['Mean_Peak_Amplitude'])
        Mean_Offset_Amplitude = float(request.POST['Mean_Offset_Amplitude'])
        Heart_Rate_BPM = float(request.POST['Heart_Rate_BPM'])

        input_data = [[Mean_Pulse_Width_at_Half_Height, Mean_Peak_to_Peak_Interval, Mean_Pulse_Interval,
                    Mean_Peak_Values_PPG_2, Mean_Offset_Values_PPG_2, Mean_Peak_Time_Interval_of_PPG_2,
                    Mean_Offset_Time_Interval_of_PPG_2, Mean_Systolic_Peak_Time, Mean_Peak_Amplitude,
                    Mean_Offset_Amplitude, Heart_Rate_BPM]]
        
        # Get the prediction for diastolic blood pressure
        diastolic_blood_pressure_prediction = model.predict(input_data)

        return render(request, 'main.html', {'result': diastolic_blood_pressure_prediction})
    return render(request, 'main.html')


# # views.py
# from django.shortcuts import render
# import h2o

# # Initialize H2O
# h2o.init()

# # Load the H2O saved model
# h2o_model = h2o.load_model('./savedmodels/Grid_DRF_py_2_sid_8fad_model_python_1699852727981_2_model_5')

# # Define the feature names in the same order as they were used during training
# feature_names = [
#     'Mean_Pulse_Width_at_Half_Height',
#     'Mean_Peak_to_Peak_Interval',
#     'Mean_Pulse_Interval',
#     'Mean Peak Values PPG\'\'',
#     'Mean Offset Values PPG\'\'',
#     'Mean Peak Time Interval of PPG\'\'',
#     'Mean Offset Time Interval of PPG\'\'',
#     'Mean Systolic Peak Time',
#     'Mean Peak Amplitude',
#     'Mean Offset Amplitude',
#     'Heart Rate (BPM)'
# ]

# def predictor(request):
#     if request.method == 'POST':
#         # Print the keys in request.POST for debugging
#         print(request.POST.keys())

#         # Extract the input values from the form
#         input_values = [float(request.POST.get(feature, 0)) for feature in feature_names]

#         # Create an H2O Frame with the input data
#         input_data = h2o.H2OFrame([[val] for val in input_values], column_names=feature_names)

#         # Make predictions using the H2O model
#         prediction = h2o_model.predict(input_data).as_data_frame()['predict'][0]

#         return render(request, 'main.html', {'prediction': prediction, 'feature_names': feature_names})
#     return render(request, 'main.html')
