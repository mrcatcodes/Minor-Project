from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Sample dataset of financial literacy levels (simplified for illustration)
users_data = [
    {'user_id': 1, 'age': 25, 'income': 3000, 'education_level': 'basic'},
    {'user_id': 2, 'age': 40, 'income': 5000, 'education_level': 'advanced'},
    {'user_id': 3, 'age': 30, 'income': 2000, 'education_level': 'intermediate'},
    {'user_id': 4, 'age': 50, 'income': 1500, 'education_level': 'basic'}
]

# Convert categorical data ('education_level') to numerical data
label_encoder = LabelEncoder()
for user in users_data:
    user['education_level'] = label_encoder.fit_transform([user['education_level']])[0]

# Convert user data into a NumPy array
user_features = np.array([[user['age'], user['income'], user['education_level']] for user in users_data])

# Create a model to suggest educational content based on nearest neighbors
model = NearestNeighbors(n_neighbors=1)  # K=1 for the nearest neighbor
model.fit(user_features)

def recommend_content(user_input):
    # Input data for new user
    new_user = np.array([user_input])  # Input should contain [age, income, education_level]
    
    # Find the nearest neighbor (most similar user)
    neighbor = model.kneighbors(new_user, return_distance=False)
    
    # Get the most similar user’s financial education level and recommend content
    similar_user = users_data[neighbor[0][0]]
    education_level = label_encoder.inverse_transform([similar_user['education_level']])[0]
    
    # Based on education level, recommend appropriate content
    content = {
        'basic': "Beginner financial literacy course",
        'intermediate': "Intermediate financial management course",
        'advanced': "Advanced investing course"
    }
    
    return content[education_level]

# Example usage
new_user_input = [35, 2500, 1]  # New user (age, income, education_level: 'intermediate')
recommended_content = recommend_content(new_user_input)
print(f"Recommended Content: {recommended_content}")
