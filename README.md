### Group Allocation Algorithm Design
This is a final assignment of Nanyang Technological University in 2025, Semester 1, class SC1003. 
### Table of Contents

### Overview
This project is given a sheet contains personal info of 6000 students, 120 tutorial groups, including:
- Tutorial Group (e.g. "G-1", "G-28")
- Student ID
- School
- Name
- Gender
- CGPA
Our goal is to introduce an algorithm, which can allocate students within same tutorial group to 10 different teams, each teams contains 5 students. The requirements of grouping is that:
- CGPA should be average, i.e. no single team's CGPA extremely higher/lower than others
- Gender should be balance, i.e. team members cannot be all boys/all girls
- School should be diverse, i.e. team members should from different schools, if possible

### Features
- Entropy Method
- Greedy Algorithm
- Simulated Annealing
- Heat-map Visualisation

### Project Structure

```
.
├── FEL2_Group4_YuJingyao
│   ├── assets
│   │   ├── 10in1.png
│   │   ├── ai_declaration
│   │   │   ├── BuChenfei_1.1.jpg
│   │   │   ├── BuChenfei_1.2.jpg
│   │   │   ├── BuChenfei_1.3.jpg
│   │   │   ├── BuChenfei_1.4.jpg
│   │   │   ├── BuChenfei_1.5.jpg
│   │   │   ├── BuChenfei_2.1.jpg
│   │   │   ├── BuChenfei_2.2.jpg
│   │   │   ├── BuChenfei_2.3.jpg
│   │   │   ├── BuChenfei_2.4.jpg
│   │   │   ├── BuChenfei_2.5.jpg
│   │   │   ├── ChenSijing_1.1.jpg
│   │   │   ├── ChenSijing_1.2.jpg
│   │   │   ├── ChenSijing_1.3.jpg
│   │   │   ├── ChenSijing_1.4.jpg
│   │   │   ├── ChenSijing_2.1.jpg
│   │   │   ├── ChenSijing_2.2.jpg
│   │   │   ├── ChenSijing_2.3.jpg
│   │   │   ├── ChenSijing_2.4.jpg
│   │   │   ├── YuJingyao_1.png
│   │   │   ├── YuJingyao_2.png
│   │   │   ├── ZhangYiran_1.jpg
│   │   │   ├── ZhangYiran_2.jpg
│   │   │   └── ZhangYiran_3.jpg
│   │   ├── anneal_res_34.png
│   │   ├── distribution_of_CGPA.png
│   │   ├── distribution_of_male_ratio.png
│   │   ├── distribution_of_school_diversity.png
│   │   ├── entropy_method_flowchart.png
│   │   ├── greedy_res_1.png
│   │   ├── greedy_res_2.png
│   │   ├── greedy_res_3.png
│   │   ├── greedy_res_34.png
│   │   ├── heatmap_test.png
│   │   ├── output.csv
│   │   ├── records.csv
│   │   ├── selection_greedy.png
│   │   ├── selection_random.png
│   │   ├── selection_simulate.png
│   │   ├── weight_cgpa.png
│   │   ├── weight_entropy.png
│   │   ├── weight_gender.png
│   │   └── weight_school.png
│   ├── FEL2_Group4_YuJingyao.csv
│   ├── FEL2_Group4_YuJingyao.ipynb
│   └── requirements.txt
└── Mini Project Requirements - Student.pdf
```

### Installation
```
git clone https://github.com/yujingyao-dev/NTU_SC1003_mini_project_25S1.git
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```
Then open the file `FEL2_Group4_YuJingyao.ipynb` 

### Contributors
- I, Yu Jingyao, the main editor and contributor, adjust and optimise the algorithm, writing, constructing, and managing the whole structure of this project, also in charge of the visualisation and data analysis.  
- Zhang Yiran, my partner, designed the greedy algorithm and scoring criteria. 
- Chen Sijing, my partner, designed the simulated annealing. 
- Bu Chenfei, my partner, designed the import/export of CSV file, also introducing the Entropy Method. 

### License
[MIT License](LICENSE)

### Acknowledgment
- I thank my parents and the whole family behind me.
- I thank my dear partners who contribute to the program a lot.
- I thank NTU who provides with a platform and an opportunity.
- I thank my TA who checked our assignments and gave a positive feedback.
- I thank myself who attempts to upload his project publicly and steps into the world of coding. 
- I thank Lin Kexin, and I promise to give you a whole life. 



