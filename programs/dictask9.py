
data = {
    'Sales': {
        'North': {
            'Alice': 'Manager',
            'Bob': 'Sales Executive',
            'Eve': 'Sales Coordinator',
            'John': 'Account Manager'
        },
        'South': {
            'Charlie': 'Sales Executive',
            'Grace': 'Regional Sales Manager',
            'Mallory': 'Business Development Associate'
        },
        'West': {
            'Oscar': 'Sales Executive',
            'Peggy': 'Account Executive',
            'Victor': 'Territory Sales Manager'
        }
    },
    'Marketing': {
        'Digital': {
            'David': 'SEO Specialist',
            'Hannah': 'Content Strategist',
            'Irene': 'Social Media Manager'
        },
        'Offline': {
            'Eve': 'Event Coordinator',
            'Jake': 'Brand Manager',
            'Liam': 'Public Relations Specialist'
        },
        'Research': {
	            'Mia': 'Market Research Analyst',
            'Noah': 'Customer Insights Manager'
        }
    },
    'IT': {
        'Infrastructure': {
            'Quinn': 'Network Engineer',
            'Riley': 'System Administrator',
            'Sam': 'Cloud Architect'
        },
        'Development': {
            'Tina': 'Software Engineer',
            'Uma': 'Backend Developer',
            'Walter': 'Full Stack Developer'
        }
    },
    'HR': {
        'Recruitment': {
            'Yara': 'Recruitment Specialist',
            'Zane': 'Talent Acquisition Manager',
            'Nina': 'HR Coordinator'
        },
        'Employee Relations': {
            'Oliver': 'Employee Relations Specialist',
            'Sophia': 'HR Business Partner'
        }
    },
    'Finance': {
        'Accounting': {
            'Xander': 'Accountant',
            'Yvette': 'Accounts Payable Specialist',
            'Zara': 'Financial Analyst'
        },
        'Audit': {
            'Luna': 'Internal Auditor',
            'Mason': 'Compliance Officer'
        }
    }
}


for key,value in data.items():
    print(key)
    print("-------------")
    for key in data[key].keys():
        print(key)
    print()