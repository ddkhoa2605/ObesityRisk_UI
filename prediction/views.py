import numpy as np
import pandas as pd
from django.shortcuts import render
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# Load model từ file đã lưu
def load_model():
    model = tf.keras.models.load_model("prediction/model/model2.h5")
    # Recompile the model to initialize metrics
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

map_yesno = {'yes': 1, 'no': 0}
map_gender = {'Male': 1, 'Female': 0}
map_CAEC = {'Sometimes': 4, 'Frequently': 3, 'Always': 2, 'no': 1}
map_MTRANS = {'Public_Transportation': 0, 'Automobile': 1, 'Walking': 2, 'Motorbike': 3, 'Bike': 4}
map_CALC = {'Sometimes': 1, 'Frequently': 2, 'no': 0}
map_target = {0: 'Insufficient_Weight', 1: 'Normal_Weight', 2: 'Overweight_Level_I', 
              3: 'Overweight_Level_II', 4: 'Obesity_Type_I', 5: 'Obesity_Type_II', 6: 'Obesity_Type_III'}

ordered_features = ['Gender', 'Age', 'Height', 'Weight', 'family_history_with_overweight', 'FAVC', 'FCVC', 'NCP', 
                    'CAEC', 'SMOKE', 'CH2O', 'SCC', 'FAF', 'TUE', 'CALC', 'MTRANS']

def predict_view(request):
    if request.method == 'POST':
        try:
            data = {
                'Gender': map_gender[request.POST['Gender']],
                'family_history_with_overweight': map_yesno[request.POST['family_history_with_overweight']],
                'FAVC': map_yesno[request.POST['FAVC']],
                'CAEC': map_CAEC[request.POST['CAEC']],
                'SMOKE': map_yesno[request.POST['SMOKE']],
                'SCC': map_yesno[request.POST['SCC']],
                'CALC': map_CALC[request.POST['CALC']],
                'MTRANS': map_MTRANS[request.POST['MTRANS']],
                'Age': float(request.POST['Age']),
                'Height': float(request.POST['Height']),
                'Weight': float(request.POST['Weight']),
                'FCVC': float(request.POST['FCVC']),
                'NCP': float(request.POST['NCP']),
                'CH2O': float(request.POST['CH2O']),
                'FAF': float(request.POST['FAF']),
                'TUE': float(request.POST['TUE'])
            }

            df = pd.DataFrame([data])
            df = df[ordered_features]
            
            model = load_model()
            prediction = model.predict(df)
            result = map_target.get(np.argmax(prediction), 'Unknown')
            
            return render(request, 'prediction.html', {'result': result})
        except KeyError as e:
            return render(request, 'prediction.html', {'error': f"Missing or invalid input: {e}"})
        except Exception as e:
            return render(request, 'prediction.html', {'error': f"Error occurred: {e}"})
    
    return render(request, 'prediction.html')
