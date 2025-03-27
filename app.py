from flask import Flask, request, render_template
from Activity import ActivityBST  # Import the ActivityBST class

app = Flask(__name__)
activity_tree = ActivityBST()  # Create an instance of ActivityBST

# Home route to show the interface
@app.route('/')
def home():
    return render_template('index.html')

# Add activity route
@app.route('/add', methods=['POST'])
def add_activity():
    try:
        duration = int(request.form['duration'])
        activity_type = request.form['activity_type']
        activity_tree.add_activity(duration, activity_type)
        return f"Activity {activity_type} ({duration} minutes) added successfully!"
    except ValueError:
        return "Invalid input. Please try again."

# Delete activity route
@app.route('/delete', methods=['POST'])
def delete_activity():
    try:
        duration = int(request.form['duration'])
        activity_tree.delete_activity(duration)
        return f"Activity with duration {duration} deleted successfully!"
    except ValueError:
        return "Invalid input. Please try again."

# Search activity route
@app.route('/search', methods=['GET'])
def search_activity():
    duration = request.args.get('duration', type=int)
    activity_type = request.args.get('activity_type', type=str)
    results = activity_tree.search_activity(duration=duration, activity_type=activity_type)
    return render_template('search_results.html', results=results)

# Statistics route
@app.route('/stats')
def view_stats():
    stats = activity_tree.generate_statistics()
    return render_template('statistics.html', stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
