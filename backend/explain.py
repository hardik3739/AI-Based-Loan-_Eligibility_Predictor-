import shap
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def get_explanation(model, input_data: pd.DataFrame):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_data)
    
    if isinstance(shap_values, list):
        vals = shap_values[1][0]
    else:
        # Depending on SHAP & sklearn versions, sometimes it's a 2D array and we just get [0]
        # or 3D where 2nd axis is class
        if len(shap_values.shape) == 3:
            vals = shap_values[0, :, 1]
        else:
            vals = shap_values[0]
            
    feature_names = input_data.columns.tolist()
    
    # SHAP impact mapped to feature name
    impacts = {feature_names[i]: float(vals[i]) for i in range(len(feature_names))}
    
    # Get top 3 factors affecting the decision
    sorted_impacts = dict(sorted(impacts.items(), key=lambda item: abs(item[1]), reverse=True)[:3])
    
    return sorted_impacts
