def check_agreement(subject, verb):
    singular_subjects = ['he', 'she', 'it']
    plural_subjects = ['they', 'we', 'you']
    
    if subject.lower() in singular_subjects and verb.endswith('s'):
        return "■ Correct agreement"
    elif subject.lower() in plural_subjects and not verb.endswith('s'):
        return "■ Correct agreement"
    else:
        return "■ Agreement error"

# Test cases
print(check_agreement('He', 'runs'))  # Expected output: ■ Correct agreement
print(check_agreement('They', 'run'))  # Expected output: ■ Correct agreement
print(check_agreement('They', 'runs'))  # Expected output: ■ Agreement error

---------------------------------OUTPUT-----------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python Act_SentcAgreement.py
■ Correct agreement
■ Correct agreement
■ Agreement error
