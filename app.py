from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    links = {
        'Class Enrollment & Prep': [
            {
                'title': 'Madgrades',
                'url': 'https://madgrades.com',
                'description': 'Find class grade distributions to help pick classes',
                'image': 'static/images/madgrades_logo.png'
            },
            {
                'title': 'MadCal',
                'url': 'https://madgrades.com',
                'description': 'Automatically add your class schedule to Google Calendar or Outlook',
                'image': 'static/images/madcal_logo.png'
            },
            {
                'title': 'enRollBadge',
                'url': 'https://enrollbadge.com',
                'description': 'Receive notifications when your desired classes become open or waitlisted',
                'image': 'static/images/enrollbadge_logo.png'
            }
            # Add more links as needed
        ],
        'Housing': [
            {
                'title': 'MadHousing',
                'url': 'https:/madhousing.com',
                'description': 'View dorm rankings from your fellow students.',
                'image': 'static/images/madhousing_logo.png'
            },
            {
                'title': 'Non-University Housing',
                'url': 'https://www.rentcollegepads.com/off-campus-housing/madison/search',
                'description': '"Finding UW-Madison rentals has never been easier"',
                'image': 'static/images/college_pads_logo.png'
            },
            # Add more links as needed
        ],
        'Entertainment': [
            {
                'title': 'BadNewsBadgers',
                'url': 'https://www.instagram.com/badnewsbadgers/',
                'description': 'Madison’s best satire & comedy page',
                'image': 'static/images/bnb_logo.JPG'
            },
            {
                'title': 'Badger Barstool',
                'url': 'https://www.instagram.com/badgerbarstool/',
                'description': 'Campus news & content',
                'image': 'static/images/barstool_logo.png'
            },
            {
                'title': 'Wisco Chicks',
                'url': 'https://www.instagram.com/wiscochicks/',
                'description': 'Campus news & content (for "chicks")',
                'image': 'static/images/wisco_chicks_logo.png'
            },
            
            
            # Add more links as needed
        ],
        'All-Campus Clubs': [
            {
                'title': 'NAMI UW',
                'url': 'https://www.instagram.com/badnewsbadgers/',
                'description': 'A student organization dedicated to promoting mental health and fighting the stigma against mental illness through education, advocacy and support',
                'image': 'static/images/nami_logo.png'
            },
            {
                'title': 'Student Leadership Program',
                'url': 'https://www.instagram.com/badgerbarstool/',
                'description': 'Work towards a leadership minor while developing effective and essential leadership skills through comprehensive leadership education and diverse experiences',
                'image': 'static/images/slp_logo.png'
            },
            # Add more links as needed
        ],
        # Add other sections as needed
    }

    return render_template('index.html', links=links)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
