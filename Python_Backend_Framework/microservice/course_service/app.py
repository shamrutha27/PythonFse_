from flask import Flask, request, jsonify
from config import Config
from models import db, Course

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


# -------------------------
# Get All Courses
# -------------------------
@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify({course.id: course.to_dict() for course in courses})


# -------------------------
# Get Course By ID
# -------------------------
@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    return jsonify(course.to_dict())


# -------------------------
# Create Course
# -------------------------
@app.route("/api/courses", methods=["POST"])
def create_course():

    data = request.json

    course = Course(
        code=data["code"],
        name=data["name"],
        instructor=data["instructor"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201


# -------------------------
# Update Course
# -------------------------
@app.route("/api/courses/<int:id>", methods=["PUT"])
def update_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    data = request.json

    course.code = data["code"]
    course.name = data["name"]
    course.instructor = data["instructor"]

    db.session.commit()

    return jsonify(course.to_dict())
@app.route("/")
def home():
    return "Course Service Running Successfully!"


# -------------------------
# Delete Course
# -------------------------
@app.route("/api/courses/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted"})


if __name__ == "__main__":
    app.run(port=5001, debug=True)