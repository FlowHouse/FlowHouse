from flask import Flask, jsonify, request
from flask_json import FlaskJSON, json_response
import peewee
from app import app
from app.models.user import User
from app.models.state import State



@app.route('/users', methods=['GET'])
def list_users():
	'''
	Get all users
	This will list all users in the database
	---
	tags: - User
	responses:
      200:
        description: return list of all users
        schema:
          id: Users
          properties:
		  	users:
              type: array
              description: array of users
	'''
	users = []
	for user in User.select():
		users.append(user.to_hash())
	return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
	'''
	Create a new user
	Creates a new users and appends to database
	---
	tags: - User
	parameters:
		-
			name: email
			in: form
			type: string
			required: True
			description: email of the user

		-
			name: frist_name
			in: form
			type: string
			required: True
			description: first name of the user
		-
			name: last_name
			in: form
			type: string
			required: True
			description: last name of the user
		-
			name: password
			in: form
			type: string
			required: True
			description: password of the user

	responses:
		409:
			description: email already exists
	'''

	try:
		user = User.create(
			email=str(request.form['email']),
			first_name=str(request.form['first_name']),
			last_name=str(request.form['last_name']),
			password=str(request.form['password'])
		)
		return jsonify(user)
	except:
		return jsonify({'code' : 10000, 'msg' : "Email already exists"}), 409


@app.route('/users/<user_id>', methods=['GET'])
def list_user_by_id(user_id):
	'''
	Get user by id
	list of the given user using user_id in databse
	---
	tags: User


	'''
	user_ids = User.get(User.id == user_id)
	try:
		for user_id in User.select():
			user_ids.append(user_id.to_hash())
		return jasonify(user_ids)
	except:
		return jsonify({'msg' : abort}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user_by_id():
	user_ids = User.get(User.id == user_id)
	for key in request.values:
		if key == 'email':
			return jsonify({'msg' : 'email can not be changed'}), 409
		if key == 'updated_at' or key == 'created_at':
			 continue
		else:
			 setattr(user_found, key, request.values.get(key))
	user.save()
	return jsonify(user), 200


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id():
	user_ids = User.get(User.id == user_id)
	try:
		for user_id in User.select():
			user_ids.delete_instance()
			users.save()
		return jsonify({'code' : 200, 'msg' : 'success'}), 200
	except:
		return jsonify({'code' : 404, 'msg' : 'not delted'}), 404
