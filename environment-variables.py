from flask import Flask, Response
import os
app = Flask(__name__)

@app.route('/')
def env_var():
	env_var_dict = os.environ
	env_var_str = ''

	for k, v in env_var_dict.iteritems():
		env_var_str += str(k) + ': ' + str(v) + '\n'

	return Response(env_var_str, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)