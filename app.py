from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop_page():
    try:
        # Get username and hostname
        name = 'sample_name'
        username = os.environ.get('USER', 'code-space')

        # Get server time
        server_time = subprocess.check_output(['date']).decode().strip()

     
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode(errors='ignore')

        response = f"""
        Name: {name}
        user: {username}
        Server Time (IST): {server_time}

        TOP output:
        {top_output}
        """

        return f"<pre>{response}</pre>"

    except subprocess.CalledProcessError as e:
        return f"Error while fetching top output: {str(e)}", 500
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
