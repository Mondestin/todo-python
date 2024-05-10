from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from classes.schema_dto import Todo, TodoNoID
from database.firebase import db

router= APIRouter(
    prefix='/todos',
    tags=["todos"]
)

# Endpoints
@router.get('/', response_model=List[Todo])
async def get_todo():
     # Query all todos' data from Firebase
    todos_data = db.child('todos').get().val()

    if todos_data is not None:
        # Convert the dictionary of Todo data into a list of Todo objects
        todo_list = [Todo(**data) for data in todos_data.values()]
        # Return the list of Todo data
        return todo_list
    else:
        # Return an empty list if no Todo data is found
        return []

# create new todos 
@router.post('/', response_model=Todo, status_code=201)
async def create_todo(givenName:TodoNoID):
    # generate unique id
    generatedId=uuid.uuid4()
    # creation of Todo object
    newtodo= Todo(id=str(generatedId), name=givenName.name)
     # Save the new Todo in Firebase
    db.child('todos').child(generatedId).set(newtodo.dict())
    # Return the created Todo
    return newtodo


@router.get('/{todo_id}', response_model=Todo)
async def get_todo_by_ID(todo_id:str):
     # Query the Todo by ID from Firebase
    todo_data = db.child('todos').child(todo_id).get().val()
    if todo_data is not None:
        return Todo(**todo_data)
    else:
        raise HTTPException(status_code=404, detail="Todo not found")


@router.patch('/{todo_id}', status_code=204)
async def modify_todo_name(todo_id:str, modifiedtodo: TodoNoID):
    # Query the Todo by ID from Firebase
    todo_data = db.child('todos').child(todo_id).get().val()

    if todo_data is not None:
        # Update the Todo's data with the provided fields
        updated_fields = modifiedtodo.dict(exclude_unset=True)
        db.child('todos').child(todo_id).update(updated_fields)

        # Return the updated Todo data
        updated_todo_data = {**todo_data, **updated_fields}
        return Todo(**updated_todo_data)
    else:
        raise HTTPException(status_code=404, detail="Todo not found")


@router.delete('/{todo_id}', status_code=204)
async def delete_todo(todo_id:str):
    # Query the Todo by ID from Firebase
    todo_data = db.child('todos').child(todo_id).get().val()

    if todo_data is not None:
        # Delete the Todo's data
         db.child('todos').child(todo_id).remove()
    else:
        raise HTTPException(status_code=404, detail="Todo not found")