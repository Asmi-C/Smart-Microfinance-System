import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/user_data.csv', header=None, names=['income', 'employment_years', 'loan_amount', 'business_experience', 'credit_history', 'loan_approved'])

approval_counts = data['loan_approved'].value_counts().rename(index={1: 'Approved', 0: 'Rejected'})
plt.figure(figsize=(6, 4))
sns.barplot(x=approval_counts.index, y=approval_counts.values)
plt.title('Loan Approval Statistics')
plt.xlabel('Status')
plt.ylabel('Number of Applications')
plt.show()
