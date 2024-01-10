Env=$1
rm source.zip
cd src/
zip -r ../source.zip . -x "*/tests/*" -x "*/__pycache__/*"
cd ..
