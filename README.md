https://github.com/conda-forge/miniforge
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh


Finally, you can run the command to activate the base environment
conda activate base
conda deactivate

pip install --upgrade pip setuptools wheel
pip install uvicorn  
uvicorn main:app --reload
pip install fastapi\[all\] sqlalchemy bcrypt python-jose email-validator aiohttp passlib jose



//swagger api list
http://localhost:8000/docs

//DB commands
sqlite3 users.db   //to launch
.tables
SELECT * FROM users;
