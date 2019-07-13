# must first run command `pip install pandas`
import pandas as pd 

# Load training data
ProviderTrainingData = pd.read_csv("Train-1542865627584.csv")
BeneficiaryTrainingData = pd.read_csv("Train_Beneficiarydata-1542865627584.csv")
InpatientClaimsTrainingData = pd.read_csv("Train_Inpatientdata-1542865627584.csv")
OutpatientClaimsTrainingData = pd.read_csv("Train_Outpatientdata-1542865627584.csv")

# Show rows/columns of each data
# print('Provider Training Data: ', ProviderTrainingData.shape, '\n', ProviderTrainingData.head(2))
# print('\n\nBeneficiary Training Data: ', BeneficiaryTrainingData.shape, '\n', BeneficiaryTrainingData.head(2))
# print('\n\nInpatient Claims Training Data ', InpatientClaimsTrainingData.shape, '\n', InpatientClaimsTrainingData.head(2))
# print('\n\nOutpatient Claims Training Data ', OutpatientClaimsTrainingData.shape, '\n', OutpatientClaimsTrainingData.head(2))

# Merge inpatient claims data with patient data
# User inner join since we only want records where beneficiary exist in both tables
InpatientClaimsWithBeneficiaryData = pd.merge(InpatientClaimsTrainingData,BeneficiaryTrainingData, on='BeneID',how='inner');
print('\nMerged inpatient claims data with beneficiary data\n\n', InpatientClaimsWithBeneficiaryData.head(5))

# Merge outpatient claims data with patient data
# User inner join since we only want records where beneficiary exist in both tables
OutpatientClaimsWithBeneficiaryData = pd.merge(OutpatientClaimsTrainingData,BeneficiaryTrainingData, on='BeneID',how='inner');
print('\nMerged outpatient claims data with beneficiary data\n\n', OutpatientClaimsWithBeneficiaryData.head(5))

# Merge InpatientClaimsWithBeneficiaryData with provider data
# User inner join since we only want records where provider exist in both tables
InpatientClaimsWithBeneficiaryDataWithProvider = pd.merge(InpatientClaimsWithBeneficiaryData,ProviderTrainingData, on='Provider',how='inner');
print('\nMerged inpatient claims data with beneficiary data with provider data\n\n', InpatientClaimsWithBeneficiaryDataWithProvider.head(5))

# Merge OutpatientClaimsWithBeneficiaryData with provider data
# User inner join since we only want records where provider exist in both tables
OutpatientClaimsWithBeneficiaryDataWithProvider = pd.merge(OutpatientClaimsWithBeneficiaryData,ProviderTrainingData, on='Provider',how='inner');
print('\nMerged outpatient claims data with beneficiary data with provider data\n\n', OutpatientClaimsWithBeneficiaryDataWithProvider.head(5))

# Save InpatientClaimsWithBeneficiaryData with provider data to file 
InpatientClaimsWithBeneficiaryDataWithProvider.to_csv('InpatientClaimsWithBeneficiaryDataWithProvider.csv', index=True)

# Save OutpatientClaimsWithBeneficiaryData with provider data to file 
OutpatientClaimsWithBeneficiaryDataWithProvider.to_csv('OutpatientClaimsWithBeneficiaryDataWithProvider.csv', index=True)