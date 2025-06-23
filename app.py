from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)

# HTML template for the home page
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeetCode Solutions Flask App</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            max-width: 800px;
            width: 90%;
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 1rem;
            font-size: 2.5rem;
        }
        .subtitle {
            color: #666;
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }
        .feature-card {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        .feature-card h3 {
            color: #333;
            margin-bottom: 0.5rem;
        }
        .feature-card p {
            color: #666;
            margin: 0;
        }
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            font-size: 1rem;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            margin: 0.5rem;
            transition: transform 0.3s ease;
        }
        .btn:hover {
            transform: translateY(-2px);
        }
        .api-section {
            margin-top: 2rem;
            padding: 1.5rem;
            background: #f8f9fa;
            border-radius: 10px;
        }
        .stats {
            display: flex;
            justify-content: space-around;
            margin: 1rem 0;
        }
        .stat-item {
            text-align: center;
        }
        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
        }
        .stat-label {
            color: #666;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 LeetCode Solutions</h1>
        <p class="subtitle">A Flask-powered workspace for coding challenges</p>
        
        <div class="stats">
            <div class="stat-item">
                <div class="stat-number">{{ solution_count }}</div>
                <div class="stat-label">Solutions</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{{ python_count }}</div>
                <div class="stat-label">Python Files</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{{ sql_count }}</div>
                <div class="stat-label">SQL Files</div>
            </div>
        </div>

        <div class="feature-grid">
            <div class="feature-card">
                <h3>📊 Solution Analytics</h3>
                <p>View statistics and insights about your coding solutions</p>
            </div>
            <div class="feature-card">
                <h3>🔍 File Explorer</h3>
                <p>Browse and search through your solution files</p>
            </div>
            <div class="feature-card">
                <h3>📈 Progress Tracking</h3>
                <p>Monitor your coding journey and improvement</p>
            </div>
        </div>

        <div class="api-section">
            <h3>🛠️ Available API Endpoints</h3>
            <a href="/api/files" class="btn">📁 List Files</a>
            <a href="/api/stats" class="btn">📊 Get Stats</a>
            <a href="/api/health" class="btn">💚 Health Check</a>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Home page with overview of the LeetCode solutions workspace"""
    # Count different types of files
    files = os.listdir('.')
    python_files = [f for f in files if f.endswith('.py') and f != 'app.py']
    sql_files = [f for f in files if f.endswith('.sql')]
    
    return render_template_string(HOME_TEMPLATE, 
                                solution_count=len(python_files) + len(sql_files),
                                python_count=len(python_files),
                                sql_count=len(sql_files))

@app.route('/api/files')
def list_files():
    """API endpoint to list all solution files"""
    try:
        files = os.listdir('.')
        solution_files = [f for f in files if f.endswith(('.py', '.sql')) and f != 'app.py']
        
        # Categorize files
        python_files = [f for f in solution_files if f.endswith('.py')]
        sql_files = [f for f in solution_files if f.endswith('.sql')]
        
        return jsonify({
            'success': True,
            'data': {
                'total_files': len(solution_files),
                'python_files': python_files,
                'sql_files': sql_files,
                'all_files': sorted(solution_files)
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/stats')
def get_stats():
    """API endpoint to get workspace statistics"""
    try:
        files = os.listdir('.')
        solution_files = [f for f in files if f.endswith(('.py', '.sql')) and f != 'app.py']
        
        # Extract problem numbers for analysis
        problem_numbers = []
        for file in solution_files:
            if file.split('.')[0].isdigit():
                problem_numbers.append(int(file.split('.')[0]))
        
        stats = {
            'total_solutions': len(solution_files),
            'python_solutions': len([f for f in solution_files if f.endswith('.py')]),
            'sql_solutions': len([f for f in solution_files if f.endswith('.sql')]),
            'problem_range': {
                'min': min(problem_numbers) if problem_numbers else 0,
                'max': max(problem_numbers) if problem_numbers else 0
            },
            'recent_files': sorted(solution_files)[-5:]  # Last 5 files alphabetically
        }
        
        return jsonify({
            'success': True,
            'data': stats
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health')
def health_check():
    """API endpoint for health check"""
    return jsonify({
        'status': 'healthy',
        'app': 'LeetCode Solutions Flask App',
        'version': '1.0.0'
    })

@app.route('/api/file/<filename>')
def get_file_content(filename):
    """API endpoint to get content of a specific file"""
    try:
        # Security check - only allow reading solution files
        if not filename.endswith(('.py', '.sql')) or filename == 'app.py':
            return jsonify({
                'success': False,
                'error': 'File type not allowed'
            }), 403
        
        if not os.path.exists(filename):
            return jsonify({
                'success': False,
                'error': 'File not found'
            }), 404
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return jsonify({
            'success': True,
            'data': {
                'filename': filename,
                'content': content,
                'size': len(content),
                'lines': len(content.split('\n'))
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Development server configuration
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print(f"🚀 Starting LeetCode Solutions Flask App...")
    print(f"📍 Running on http://localhost:{port}")
    print(f"🔧 Debug mode: {debug}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
