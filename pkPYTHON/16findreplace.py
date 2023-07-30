#for finding double space

st="you are very lazy  i really don\'t like you."
doublespace=st.find("  ")
print(doublespace)
doublespace=st.replace("  "," and ")
print(doublespace)

