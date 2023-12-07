def query_builder(start= "2020", finish = "2023", med = "ASPIRIN", speed_limit="50", sex_input = ""):

  date_range = f"(receivedate:[{start}0101+TO+{finish}1207])"

  speed = f"&limit={speed_limit}"

  product = f'+AND+patient.drug.medicinalproduct:"{med}"'

  if sex_input != "":
  
    sex_binary = "sex"

    sex = f'+AND+patient.patientsex:{sex_binary}'
  else: 
    sex = ""

  query_builder = f'https://api.fda.gov/drug/event.json?search={date_range}{product}{sex}{speed}'

  return query_builder


query_builder()