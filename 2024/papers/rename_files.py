import os

papers = os.listdir('.')
papers.remove('rename_files.py')
papers_names = [paper.split('.pdf')[0] for paper in papers]
assert len(papers) == len(papers_names)

check_names = []
rename_names = []
for paper in papers_names:
    if len(paper) <3:
        check_names.append(paper)
    else:
        rename_names.append(paper)

print('Check names:', len(check_names))
print('Rename names:', len(rename_names))
print('Total:', len(papers_names))

for paper in rename_names:
    paper_original_name = paper + '.pdf'
    new_name = paper + '_submitted.pdf'

    submission_number = paper.split('_')[0]
    corresponding_submission = [p for p in check_names if submission_number == p][0]

    # print(paper, new_name, submission_number, corresponding_submission)
    corresponding_submission_name = corresponding_submission + '.pdf'
    # print(paper_original_name, new_name, corresponding_submission_name, paper_original_name)
    os.rename(paper_original_name, new_name)
    os.rename(corresponding_submission_name, paper_original_name)