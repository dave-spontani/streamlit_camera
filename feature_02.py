####In this file, we build the query for the api using the inputs from the user#####
# As a failsafe, we define the inputs with a default value in order to avoid errors

def query_builder(start= "2020", finish = "2023", med = "ASPIRIN", speed_limit="50", sex_input = ""):
  # Modulate the strings with the necessary parameters
  date_range = f"(receivedate:[{start}0101+TO+{finish}1207])"
  # Define the amount of values to get back
  speed = f"&limit={speed_limit}"
  # And the type of medicine
  product = f'+AND+patient.drug.medicinalproduct:"{med}"'
  # Check if a sex-specific search should be executed. If not, we leave the string empty
  if sex_input != "":

    sex = f'+AND+patient.patientsex:{sex_input}'
  else: 
    sex = ""
  # Build the final query with the pre-defiend parameters!
  query_builder = f'https://api.fda.gov/drug/event.json?search={date_range}{product}{sex}{speed}'

  #And return it
  return query_builder
