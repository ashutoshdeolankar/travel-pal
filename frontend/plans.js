/* Sample ready-made travel plans for Vishwaara (demo content).
   Costs are rough estimates per person in rupees, excluding flights. Not real quotes. */
const TRAVEL_PLANS = {
 "Andhra Pradesh": [
  {
   "title": "Tirupati and Chandragiri",
   "days": 3,
   "season": "October to March",
   "cost": 9000,
   "itinerary": [
    "Arrive in Tirupati. Evening at Govindaraja Swamy Temple.",
    "Tirumala Venkateswara Temple darshan (book a slot online).",
    "Sri Padmavathi Temple at Tiruchanoor, Kapila Theertham, then Chandragiri Fort and departure."
   ],
   "note": ""
  },
  {
   "title": "Vizag and Araku Valley",
   "days": 4,
   "season": "October to February",
   "cost": 12000,
   "itinerary": [
    "Visakhapatnam: RK Beach and Kailasagiri.",
    "INS Kurusura Submarine Museum and Rushikonda Beach.",
    "Scenic train or road to Araku Valley, then Borra Caves.",
    "Tribal Museum, coffee plantations and return."
   ],
   "note": ""
  },
  {
   "title": "Weekend in Vijayawada and Amaravati",
   "days": 2,
   "season": "October to March",
   "cost": 5500,
   "itinerary": [
    "Kanaka Durga Temple on Indrakeeladri and Prakasam Barrage.",
    "Undavalli Caves, Amaravati Stupa and Bhavani Island."
   ],
   "note": ""
  },
  {
   "title": "Godavari and Papikondalu",
   "days": 4,
   "season": "October to February",
   "cost": 9500,
   "itinerary": [
    "Rajahmundry: Godavari ghats and the Godavari bridge.",
    "Papikondalu boat cruise from Pattiseema.",
    "Dowleswaram Barrage.",
    "Antarvedi Temple and beach, then return."
   ],
   "note": ""
  }
 ],
 "Bihar": [
  {
   "title": "Buddhist Circuit",
   "days": 4,
   "season": "October to March",
   "cost": 10000,
   "itinerary": [
    "Patna: Golghar and Patna Museum.",
    "Bodh Gaya: Mahabodhi Temple and the Great Buddha Statue.",
    "Rajgir: Vishwa Shanti Stupa, hot springs and Gridhakuta Hill.",
    "Nalanda University ruins and return."
   ],
   "note": ""
  },
  {
   "title": "Patna and Vaishali Heritage",
   "days": 3,
   "season": "October to March",
   "cost": 7000,
   "itinerary": [
    "Takht Sri Patna Sahib and Patna Museum.",
    "Vaishali: Ashokan Pillar and the Buddha Relic Stupa.",
    "Kumhrar excavation site, Khuda Bakhsh Library and departure."
   ],
   "note": ""
  },
  {
   "title": "Weekend in Bodh Gaya",
   "days": 2,
   "season": "November to February",
   "cost": 4500,
   "itinerary": [
    "Mahabodhi Temple, Bodhi Tree and the Great Buddha Statue.",
    "Thai Monastery and Dungeshwari Cave Temples."
   ],
   "note": ""
  },
  {
   "title": "Rajgir and Pawapuri",
   "days": 3,
   "season": "October to March",
   "cost": 7000,
   "itinerary": [
    "Rajgir: Vishwa Shanti Stupa by ropeway.",
    "Venu Vana and Jarasandh ka Akhara.",
    "Pawapuri Jal Mandir and return."
   ],
   "note": ""
  }
 ],
 "Tamil Nadu": [
  {
   "title": "Temple Trail",
   "days": 5,
   "season": "October to March",
   "cost": 15000,
   "itinerary": [
    "Chennai: Marina Beach and Kapaleeshwarar Temple.",
    "Mahabalipuram: Shore Temple and Pancha Rathas.",
    "Thanjavur: Brihadeeswarar Temple.",
    "Madurai: Meenakshi Amman Temple and Thirumalai Nayak Palace.",
    "Rameswaram: Ramanathaswamy Temple and Pamban Bridge."
   ],
   "note": ""
  },
  {
   "title": "Ooty and Coonoor Hills",
   "days": 4,
   "season": "March to June",
   "cost": 11000,
   "itinerary": [
    "Coimbatore to Ooty. Botanical Garden in the evening.",
    "Doddabetta Peak and Ooty Lake.",
    "Coonoor: Sim's Park and Dolphin's Nose viewpoint.",
    "Nilgiri Mountain Railway ride and return."
   ],
   "note": ""
  },
  {
   "title": "Kodaikanal Hill Break",
   "days": 3,
   "season": "March to June",
   "cost": 8500,
   "itinerary": [
    "Kodai Lake and Coaker's Walk.",
    "Pillar Rocks and Bryant Park.",
    "Silver Cascade and Berijam Lake (permit needed), then return."
   ],
   "note": ""
  },
  {
   "title": "Kanyakumari and the Southern Tip",
   "days": 4,
   "season": "October to March",
   "cost": 10500,
   "itinerary": [
    "Kanyakumari: sunrise, Vivekananda Rock Memorial and Thiruvalluvar Statue.",
    "Padmanabhapuram Palace.",
    "Suchindram Temple.",
    "Return."
   ],
   "note": ""
  }
 ],
 "Kerala": [
  {
   "title": "Backwaters and Hills",
   "days": 5,
   "season": "September to March",
   "cost": 16000,
   "itinerary": [
    "Kochi: Fort Kochi and the Chinese fishing nets.",
    "Drive to Munnar. Tea gardens and Mattupetty Dam.",
    "Eravikulam National Park and Top Station.",
    "Alleppey: overnight houseboat on the backwaters.",
    "Morning on the water, then return to Kochi."
   ],
   "note": ""
  },
  {
   "title": "Wayanad Nature Escape",
   "days": 3,
   "season": "October to May",
   "cost": 8000,
   "itinerary": [
    "Arrive in Wayanad. Pookode Lake.",
    "Edakkal Caves and Banasura Sagar Dam.",
    "Soochipara Falls and a short nature walk, then departure."
   ],
   "note": ""
  },
  {
   "title": "Fort Kochi Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 5500,
   "itinerary": [
    "Fort Kochi, Mattancherry Palace and Jew Town. Evening Kathakali show.",
    "Marine Drive and the Kerala Folklore Museum."
   ],
   "note": ""
  },
  {
   "title": "Thekkady and Kumarakom",
   "days": 4,
   "season": "September to March",
   "cost": 12500,
   "itinerary": [
    "Thekkady: Periyar Tiger Reserve boat ride.",
    "Spice plantation walk.",
    "Kumarakom Bird Sanctuary.",
    "Vembanad Lake backwater cruise and return."
   ],
   "note": ""
  }
 ],
 "Karnataka": [
  {
   "title": "Royal Mysuru and Coorg",
   "days": 5,
   "season": "October to March",
   "cost": 14000,
   "itinerary": [
    "Mysuru: Palace and Chamundi Hills.",
    "Srirangapatna and Brindavan Gardens in the evening.",
    "Drive to Coorg. Abbey Falls and Raja's Seat.",
    "Dubare Elephant Camp and a coffee estate walk.",
    "Return to Bengaluru."
   ],
   "note": ""
  },
  {
   "title": "Hampi Heritage",
   "days": 3,
   "season": "October to February",
   "cost": 8500,
   "itinerary": [
    "Hampi: Virupaksha Temple and Hemakuta Hill at sunset.",
    "Vittala Temple, Stone Chariot and Lotus Mahal.",
    "Anegundi village and a Tungabhadra coracle ride."
   ],
   "note": ""
  },
  {
   "title": "Gokarna Beach Break",
   "days": 3,
   "season": "October to February",
   "cost": 8000,
   "itinerary": [
    "Gokarna: Mahabaleshwar Temple and Gokarna Beach.",
    "Om Beach and Kudle Beach.",
    "Half Moon Beach by trek and departure."
   ],
   "note": ""
  },
  {
   "title": "Badami, Aihole and Pattadakal",
   "days": 3,
   "season": "October to February",
   "cost": 8500,
   "itinerary": [
    "Badami cave temples and Agastya Lake.",
    "Aihole temples.",
    "Pattadakal (UNESCO World Heritage) and Mahakuta."
   ],
   "note": ""
  }
 ],
 "Goa": [
  {
   "title": "North Goa Beach Break",
   "days": 3,
   "season": "November to February",
   "cost": 9500,
   "itinerary": [
    "Calangute and Baga beaches. Fort Aguada at sunset.",
    "Old Goa: Basilica of Bom Jesus. Fontainhas walk in Panaji.",
    "Anjuna flea market (Wednesdays), then departure."
   ],
   "note": ""
  },
  {
   "title": "South Goa Calm",
   "days": 4,
   "season": "November to March",
   "cost": 12000,
   "itinerary": [
    "Arrive at Palolem Beach.",
    "Agonda Beach and Cabo de Rama Fort.",
    "Dudhsagar Falls day trip.",
    "Free morning and departure."
   ],
   "note": ""
  },
  {
   "title": "Heritage Goa Weekend",
   "days": 2,
   "season": "November to February",
   "cost": 6500,
   "itinerary": [
    "Panaji: Fontainhas and Se Cathedral.",
    "Basilica of Bom Jesus and Chapora Fort."
   ],
   "note": ""
  },
  {
   "title": "Goa Nature and Waterfalls",
   "days": 4,
   "season": "October to February",
   "cost": 11000,
   "itinerary": [
    "Spice plantation near Ponda.",
    "Tambdi Surla Mahadev Temple.",
    "Dudhsagar Falls.",
    "Cotigao Wildlife Sanctuary and return."
   ],
   "note": ""
  }
 ],
 "Odisha": [
  {
   "title": "Golden Triangle of Odisha",
   "days": 4,
   "season": "October to March",
   "cost": 10000,
   "itinerary": [
    "Bhubaneswar: Lingaraj Temple and Udayagiri-Khandagiri Caves.",
    "Puri: Jagannath Temple and Puri Beach.",
    "Konark Sun Temple.",
    "Chilika Lake boat ride and return."
   ],
   "note": ""
  },
  {
   "title": "Chilika and Raghurajpur",
   "days": 3,
   "season": "November to February",
   "cost": 8500,
   "itinerary": [
    "Arrive in Puri. Evening on the beach.",
    "Satapada: dolphin watching on Chilika Lake.",
    "Raghurajpur artist village and departure."
   ],
   "note": ""
  },
  {
   "title": "Weekend in Bhubaneswar",
   "days": 2,
   "season": "October to March",
   "cost": 5500,
   "itinerary": [
    "Lingaraj, Mukteshwar and Rajarani temples.",
    "Odisha State Museum and Nandankanan Zoological Park."
   ],
   "note": ""
  },
  {
   "title": "Simlipal and Mayurbhanj",
   "days": 4,
   "season": "November to June",
   "cost": 11000,
   "itinerary": [
    "Arrive at Simlipal.",
    "Simlipal National Park safari.",
    "Barehipani and Joranda Falls.",
    "Return."
   ],
   "note": "Simlipal needs an entry permit and is closed in monsoon."
  }
 ],
 "Chhattisgarh": [
  {
   "title": "Bastar Tribal Trail",
   "days": 4,
   "season": "October to March",
   "cost": 9000,
   "itinerary": [
    "Fly to Raipur, then travel to Jagdalpur.",
    "Chitrakote Falls.",
    "Kanger Valley National Park and Tirathgarh Falls.",
    "Danteshwari Temple at Dantewada and return."
   ],
   "note": ""
  },
  {
   "title": "Raipur and Sirpur",
   "days": 3,
   "season": "October to February",
   "cost": 6500,
   "itinerary": [
    "Raipur: Mahant Ghasidas Museum and Nandan Van.",
    "Sirpur: Laxman Temple and ancient Buddhist sites.",
    "Ratanpur Mahamaya Temple and departure."
   ],
   "note": ""
  },
  {
   "title": "Mainpat Hill Station",
   "days": 3,
   "season": "October to March",
   "cost": 7500,
   "itinerary": [
    "Arrive in Mainpat.",
    "Tiger Point and Fish Point.",
    "Ulta Pani and Mehta Point, then return."
   ],
   "note": ""
  },
  {
   "title": "Barnawapara Wildlife Weekend",
   "days": 3,
   "season": "November to June",
   "cost": 7000,
   "itinerary": [
    "Raipur to Barnawapara.",
    "Jungle safari.",
    "Morning safari and return."
   ],
   "note": "The sanctuary is closed in monsoon."
  }
 ],
 "Maharashtra": [
  {
   "title": "Mumbai and Lonavala",
   "days": 4,
   "season": "October to February",
   "cost": 12000,
   "itinerary": [
    "Mumbai: Gateway of India and Marine Drive.",
    "Elephanta Caves and Colaba Causeway.",
    "Lonavala: Karla Caves and Bhushi Dam.",
    "Tiger Point and return."
   ],
   "note": ""
  },
  {
   "title": "Ajanta and Ellora",
   "days": 4,
   "season": "October to March",
   "cost": 11000,
   "itinerary": [
    "Aurangabad: Bibi Ka Maqbara.",
    "Ellora Caves (Kailasa Temple).",
    "Ajanta Caves.",
    "Daulatabad Fort and departure."
   ],
   "note": "Ellora is closed on Tuesdays and Ajanta on Mondays. Check before you go."
  },
  {
   "title": "Pune and Mahabaleshwar",
   "days": 4,
   "season": "October to February",
   "cost": 10500,
   "itinerary": [
    "Pune: Shaniwar Wada and Aga Khan Palace.",
    "Sinhagad Fort.",
    "Mahabaleshwar: Venna Lake and Arthur's Seat.",
    "Pratapgad Fort and return."
   ],
   "note": ""
  },
  {
   "title": "Konkan Coast",
   "days": 4,
   "season": "October to March",
   "cost": 10500,
   "itinerary": [
    "Ganpatipule Beach and temple.",
    "Drive to Malvan.",
    "Tarkarli Beach and Sindhudurg Fort.",
    "Return."
   ],
   "note": ""
  }
 ],
 "Punjab": [
  {
   "title": "Amritsar Weekend",
   "days": 3,
   "season": "October to March",
   "cost": 7000,
   "itinerary": [
    "Golden Temple and Jallianwala Bagh.",
    "Partition Museum and the Wagah Border ceremony.",
    "Gobindgarh Fort and local food, then departure."
   ],
   "note": ""
  },
  {
   "title": "Heritage Punjab",
   "days": 3,
   "season": "November to March",
   "cost": 7500,
   "itinerary": [
    "Patiala: Qila Mubarak.",
    "Sheesh Mahal and Moti Bagh Palace.",
    "Anandpur Sahib and Virasat-e-Khalsa museum."
   ],
   "note": ""
  },
  {
   "title": "Amritsar Food Trail",
   "days": 2,
   "season": "October to March",
   "cost": 5000,
   "itinerary": [
    "Golden Temple langar, Amritsari kulcha and Hall Bazaar.",
    "Kesar Da Dhaba, lassi stop and departure."
   ],
   "note": ""
  },
  {
   "title": "Kapurthala Royal Trail",
   "days": 3,
   "season": "November to March",
   "cost": 6500,
   "itinerary": [
    "Kapurthala: Jagatjit Palace and Moorish Mosque.",
    "Kanjli Wetland.",
    "Jalandhar: Devi Talab Mandir and return."
   ],
   "note": ""
  }
 ],
 "Madhya Pradesh": [
  {
   "title": "Kanha Tiger Trail",
   "days": 4,
   "season": "October to June",
   "cost": 14000,
   "itinerary": [
    "Arrive at Kanha.",
    "Morning and evening jeep safaris.",
    "Another full safari day.",
    "Village visit and return."
   ],
   "note": "The park is closed in monsoon, July to September."
  },
  {
   "title": "Temples and Heritage",
   "days": 5,
   "season": "October to March",
   "cost": 13000,
   "itinerary": [
    "Bhopal: Upper Lake and the state museum.",
    "Sanchi Stupa.",
    "Orchha: Raja Mahal and Chaturbhuj Temple.",
    "Khajuraho: Western Group of temples.",
    "Eastern Group and return."
   ],
   "note": ""
  },
  {
   "title": "Ujjain and Indore",
   "days": 3,
   "season": "October to March",
   "cost": 7000,
   "itinerary": [
    "Ujjain: Mahakaleshwar Temple and Ram Ghat.",
    "Indore: Rajwada and Lal Bagh Palace.",
    "Sarafa Bazaar food walk and departure."
   ],
   "note": ""
  },
  {
   "title": "Pachmarhi Hill Station",
   "days": 3,
   "season": "October to June",
   "cost": 8500,
   "itinerary": [
    "Arrive in Pachmarhi.",
    "Bee Falls and Pandav Caves.",
    "Dhoopgarh sunset and Jata Shankar, then return."
   ],
   "note": ""
  }
 ],
 "Jharkhand": [
  {
   "title": "Waterfalls Circuit",
   "days": 3,
   "season": "July to February",
   "cost": 7000,
   "itinerary": [
    "Ranchi: Rock Garden and Tagore Hill.",
    "Hundru Falls and Dassam Falls.",
    "Jonha Falls and departure."
   ],
   "note": ""
  },
  {
   "title": "Netarhat Hills",
   "days": 3,
   "season": "October to March",
   "cost": 7500,
   "itinerary": [
    "Ranchi to Netarhat. Sunset Point.",
    "Magnolia Point sunrise and Lodh Falls.",
    "Return via Ranchi."
   ],
   "note": ""
  },
  {
   "title": "Deoghar Pilgrimage",
   "days": 2,
   "season": "October to March",
   "cost": 5000,
   "itinerary": [
    "Baidyanath Dham Temple.",
    "Trikut Hill ropeway and Naulakha Mandir."
   ],
   "note": ""
  },
  {
   "title": "Betla and Palamau",
   "days": 3,
   "season": "November to March",
   "cost": 8000,
   "itinerary": [
    "Ranchi to Betla.",
    "Betla National Park safari.",
    "Palamau Fort and Lodh Falls."
   ],
   "note": ""
  }
 ],
 "West Bengal": [
  {
   "title": "Kolkata Culture Walk",
   "days": 3,
   "season": "October to March",
   "cost": 8000,
   "itinerary": [
    "Victoria Memorial and Maidan.",
    "Howrah Bridge, flower market and Dakshineswar Temple.",
    "Indian Museum, College Street and Park Street food."
   ],
   "note": ""
  },
  {
   "title": "Darjeeling Hills",
   "days": 5,
   "season": "March to May, October to November",
   "cost": 14000,
   "itinerary": [
    "Arrive in Darjeeling. Mall Road.",
    "Tiger Hill sunrise and Batasia Loop.",
    "Himalayan Mountaineering Institute and Zoo.",
    "Toy Train ride and Happy Valley Tea Estate.",
    "Return."
   ],
   "note": ""
  },
  {
   "title": "Sundarbans Boat Safari",
   "days": 3,
   "season": "October to March",
   "cost": 10000,
   "itinerary": [
    "Kolkata to Godkhali.",
    "Boat safari and Sajnekhali watch tower.",
    "Mangrove creeks and return."
   ],
   "note": "Entry permits are needed for the Sundarbans."
  },
  {
   "title": "Shantiniketan Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 5500,
   "itinerary": [
    "Visva-Bharati and Uttarayan Complex.",
    "Sonajhuri forest and Kopai river."
   ],
   "note": ""
  }
 ],
 "Delhi": [
  {
   "title": "Old and New Delhi",
   "days": 3,
   "season": "October to March",
   "cost": 8000,
   "itinerary": [
    "Red Fort, Jama Masjid and Chandni Chowk.",
    "India Gate and Humayun's Tomb.",
    "Qutub Minar and Lotus Temple."
   ],
   "note": ""
  },
  {
   "title": "Delhi Heritage and Food",
   "days": 3,
   "season": "October to March",
   "cost": 8500,
   "itinerary": [
    "Hauz Khas Village and Lodhi Garden.",
    "Akshardham and Connaught Place.",
    "Dilli Haat and street food trail."
   ],
   "note": ""
  },
  {
   "title": "Mughal Delhi",
   "days": 2,
   "season": "October to March",
   "cost": 5500,
   "itinerary": [
    "Red Fort, Jama Masjid and Chandni Chowk.",
    "Humayun's Tomb, Purana Qila and Safdarjung's Tomb."
   ],
   "note": ""
  },
  {
   "title": "Delhi with Kids",
   "days": 3,
   "season": "October to March",
   "cost": 8500,
   "itinerary": [
    "National Science Centre and Nehru Planetarium.",
    "National Zoological Park.",
    "National Rail Museum and Garden of Five Senses."
   ],
   "note": ""
  }
 ],
 "Haryana": [
  {
   "title": "Kurukshetra Heritage",
   "days": 2,
   "season": "October to March",
   "cost": 4500,
   "itinerary": [
    "Brahma Sarovar and Sri Krishna Museum.",
    "Jyotisar and Sheikh Chilli's Tomb, then departure."
   ],
   "note": ""
  },
  {
   "title": "Sultanpur and Surajkund",
   "days": 3,
   "season": "November to March",
   "cost": 7000,
   "itinerary": [
    "Sultanpur Bird Sanctuary.",
    "Surajkund and Damdama Lake.",
    "Gurugram: Kingdom of Dreams or Leisure Valley Park."
   ],
   "note": ""
  },
  {
   "title": "Pinjore and Morni Hills",
   "days": 2,
   "season": "October to March",
   "cost": 4500,
   "itinerary": [
    "Pinjore Gardens.",
    "Morni Hills and Tikkar Taal."
   ],
   "note": ""
  },
  {
   "title": "Kalesar National Park",
   "days": 2,
   "season": "October to June",
   "cost": 4500,
   "itinerary": [
    "Kalesar National Park jeep safari.",
    "Hathnikund Barrage."
   ],
   "note": ""
  }
 ],
 "Himachal Pradesh": [
  {
   "title": "Shimla and Manali",
   "days": 6,
   "season": "March to June, October to December",
   "cost": 16000,
   "itinerary": [
    "Shimla: Mall Road and The Ridge.",
    "Kufri.",
    "Drive to Manali.",
    "Hadimba Temple and Old Manali.",
    "Solang Valley.",
    "Atal Tunnel to Sissu and return."
   ],
   "note": ""
  },
  {
   "title": "Dharamshala and Dalhousie",
   "days": 4,
   "season": "March to June",
   "cost": 10500,
   "itinerary": [
    "McLeod Ganj and the Dalai Lama Temple.",
    "Bhagsu Waterfall and Triund trek (optional).",
    "Dalhousie: Subhash Baoli.",
    "Khajjiar and return."
   ],
   "note": ""
  },
  {
   "title": "Spiti Valley Road Trip",
   "days": 7,
   "season": "June to October",
   "cost": 25000,
   "itinerary": [
    "Shimla to Kalpa.",
    "Nako Lake and Tabo Monastery.",
    "Dhankar and Kaza.",
    "Key Monastery and Kibber.",
    "Langza, Hikkim and Komic.",
    "Chandratal Lake.",
    "Drive to Manali."
   ],
   "note": "Roads close in winter. Altitude sickness is possible, so go slowly."
  },
  {
   "title": "Kasol and Parvati Valley",
   "days": 4,
   "season": "March to June, September to November",
   "cost": 9500,
   "itinerary": [
    "Arrive in Kasol.",
    "Manikaran Sahib hot springs.",
    "Tosh village.",
    "Malana village and return."
   ],
   "note": ""
  }
 ],
 "Ladakh": [
  {
   "title": "Leh Classic",
   "days": 6,
   "season": "June to September",
   "cost": 24000,
   "itinerary": [
    "Arrive in Leh. Rest all day to adjust to the altitude.",
    "Leh Palace and Shanti Stupa.",
    "Magnetic Hill, Gurudwara Pathar Sahib and the Sangam.",
    "Drive to Nubra Valley over Khardung La.",
    "Diskit Monastery and Hunder sand dunes.",
    "Return to Leh."
   ],
   "note": "Rest on day 1. Inner Line Permit is needed for Nubra."
  },
  {
   "title": "Pangong Lake",
   "days": 4,
   "season": "May to September",
   "cost": 17000,
   "itinerary": [
    "Arrive in Leh and rest.",
    "Thiksey and Hemis monasteries.",
    "Pangong Lake via Chang La.",
    "Return to Leh."
   ],
   "note": "Inner Line Permit is needed for Pangong."
  },
  {
   "title": "Nubra and Turtuk",
   "days": 5,
   "season": "June to September",
   "cost": 20000,
   "itinerary": [
    "Arrive in Leh and rest.",
    "Khardung La to Nubra.",
    "Turtuk village.",
    "Hunder dunes and Diskit Monastery.",
    "Return to Leh."
   ],
   "note": "Inner Line Permit is needed."
  },
  {
   "title": "Leh Monasteries",
   "days": 4,
   "season": "June to September",
   "cost": 15000,
   "itinerary": [
    "Arrive in Leh and rest.",
    "Thiksey and Hemis monasteries.",
    "Shey Palace, Alchi and Likir.",
    "Lamayuru and return."
   ],
   "note": ""
  }
 ],
 "Uttarakhand": [
  {
   "title": "Rishikesh and Haridwar",
   "days": 3,
   "season": "September to November, February to April",
   "cost": 7000,
   "itinerary": [
    "Haridwar: Har Ki Pauri and the evening Ganga Aarti.",
    "Rishikesh: Laxman Jhula and Ram Jhula.",
    "River rafting and Beatles Ashram."
   ],
   "note": ""
  },
  {
   "title": "Mussoorie and Nainital",
   "days": 5,
   "season": "March to June",
   "cost": 13000,
   "itinerary": [
    "Mussoorie: Mall Road and Gun Hill.",
    "Kempty Falls.",
    "Drive to Nainital. Naini Lake boating.",
    "Snow View Point and Tiffin Top.",
    "Bhimtal and return."
   ],
   "note": ""
  },
  {
   "title": "Jim Corbett Weekend",
   "days": 3,
   "season": "November to June",
   "cost": 8500,
   "itinerary": [
    "Arrive at Jim Corbett.",
    "Jeep safari in Bijrani.",
    "Corbett Falls and Garjiya Devi Temple."
   ],
   "note": "Parts of the park are closed in monsoon."
  },
  {
   "title": "Valley of Flowers Trek",
   "days": 5,
   "season": "July to September",
   "cost": 14000,
   "itinerary": [
    "Haridwar to Joshimath.",
    "Govindghat to Ghangaria trek.",
    "Valley of Flowers.",
    "Hemkund Sahib.",
    "Trek down and return."
   ],
   "note": "A moderate fitness level is needed."
  }
 ],
 "Uttar Pradesh": [
  {
   "title": "Taj and Agra",
   "days": 3,
   "season": "October to March",
   "cost": 9000,
   "itinerary": [
    "Taj Mahal at sunrise and Mehtab Bagh.",
    "Agra Fort and Itimad-ud-Daulah.",
    "Fatehpur Sikri and departure."
   ],
   "note": "The Taj Mahal is closed on Fridays."
  },
  {
   "title": "Varanasi and Ayodhya",
   "days": 4,
   "season": "October to March",
   "cost": 9500,
   "itinerary": [
    "Varanasi: Kashi Vishwanath Temple and the Ganga Aarti at Dashashwamedh Ghat.",
    "Sunrise boat ride and Sarnath.",
    "Travel to Ayodhya. Ram Mandir.",
    "Hanuman Garhi and return."
   ],
   "note": ""
  },
  {
   "title": "Lucknow Nawabi Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 5500,
   "itinerary": [
    "Bara Imambara, Rumi Darwaza and the Residency.",
    "Chowk food walk and Hazratganj."
   ],
   "note": ""
  },
  {
   "title": "Mathura and Vrindavan",
   "days": 3,
   "season": "October to March",
   "cost": 7000,
   "itinerary": [
    "Mathura: Krishna Janmabhoomi.",
    "Vrindavan: Banke Bihari Temple and ISKCON.",
    "Prem Mandir and Govardhan, then return."
   ],
   "note": ""
  }
 ],
 "Telangana": [
  {
   "title": "Hyderabad Highlights",
   "days": 3,
   "season": "October to March",
   "cost": 8500,
   "itinerary": [
    "Charminar, Laad Bazaar and Chowmahalla Palace.",
    "Golconda Fort and the evening sound and light show.",
    "Hussain Sagar and Ramoji Film City."
   ],
   "note": ""
  },
  {
   "title": "Warangal Heritage",
   "days": 2,
   "season": "October to February",
   "cost": 5500,
   "itinerary": [
    "Warangal Fort and the Thousand Pillar Temple.",
    "Ramappa Temple (UNESCO World Heritage) and Laknavaram Lake."
   ],
   "note": ""
  },
  {
   "title": "Hyderabad Food and Old City",
   "days": 2,
   "season": "October to March",
   "cost": 6500,
   "itinerary": [
    "Charminar, Mecca Masjid and Irani chai.",
    "Salar Jung Museum and a biryani lunch."
   ],
   "note": ""
  },
  {
   "title": "Medak Weekend",
   "days": 2,
   "season": "October to February",
   "cost": 5000,
   "itinerary": [
    "Medak Cathedral and Medak Fort.",
    "Pocharam Wildlife Sanctuary."
   ],
   "note": ""
  }
 ],
 "Arunachal Pradesh": [
  {
   "title": "Tawang Trail",
   "days": 6,
   "season": "March to October",
   "cost": 22000,
   "itinerary": [
    "Guwahati to Bomdila.",
    "Bomdila Monastery and Dirang.",
    "Sela Pass to Tawang.",
    "Tawang Monastery and the Jaswant Garh war memorial.",
    "Sangestar (Madhuri) Lake.",
    "Return to Guwahati."
   ],
   "note": "Inner Line Permit is needed."
  },
  {
   "title": "Ziro Valley",
   "days": 4,
   "season": "March to October",
   "cost": 14000,
   "itinerary": [
    "Arrive in Ziro.",
    "Apatani villages and Hapoli.",
    "Talley Valley Wildlife Sanctuary.",
    "Meghna Cave Temple and departure."
   ],
   "note": "Inner Line Permit is needed."
  },
  {
   "title": "Pasighat and the Siang River",
   "days": 4,
   "season": "October to March",
   "cost": 13000,
   "itinerary": [
    "Fly to Dibrugarh and drive to Pasighat.",
    "Siang River rafting.",
    "Daying Ering Wildlife Sanctuary.",
    "Return."
   ],
   "note": "Inner Line Permit is needed."
  },
  {
   "title": "Itanagar Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 6500,
   "itinerary": [
    "Ita Fort and Ganga Lake.",
    "State Museum and Buddhist temple."
   ],
   "note": "Inner Line Permit is needed."
  }
 ],
 "Assam": [
  {
   "title": "Kaziranga Safari",
   "days": 4,
   "season": "November to April",
   "cost": 14000,
   "itinerary": [
    "Guwahati: Kamakhya Temple.",
    "Drive to Kaziranga.",
    "Central Range elephant or jeep safari.",
    "Western Range safari and return."
   ],
   "note": "The park is closed from May to October."
  },
  {
   "title": "Majuli and Sivasagar",
   "days": 4,
   "season": "November to March",
   "cost": 10500,
   "itinerary": [
    "Jorhat. Overnight stay.",
    "Majuli river island and a satra visit.",
    "Sivasagar: Rang Ghar and Talatal Ghar.",
    "Return."
   ],
   "note": ""
  },
  {
   "title": "Guwahati Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 6500,
   "itinerary": [
    "Kamakhya Temple and Assam State Museum.",
    "Umananda Island and Brahmaputra cruise."
   ],
   "note": ""
  },
  {
   "title": "Manas National Park",
   "days": 3,
   "season": "November to April",
   "cost": 9500,
   "itinerary": [
    "Guwahati to Manas.",
    "Jeep safari.",
    "Bansbari and return."
   ],
   "note": ""
  }
 ],
 "Chandigarh": [
  {
   "title": "City Beautiful",
   "days": 2,
   "season": "October to March",
   "cost": 4500,
   "itinerary": [
    "Rock Garden, Sukhna Lake and Rose Garden.",
    "Capitol Complex and Pinjore Gardens."
   ],
   "note": ""
  },
  {
   "title": "Chandigarh with Kasauli",
   "days": 3,
   "season": "October to March",
   "cost": 7000,
   "itinerary": [
    "Sukhna Lake and Rock Garden.",
    "Day trip to Kasauli: Christ Church and Monkey Point.",
    "Sector 17 market and departure."
   ],
   "note": ""
  },
  {
   "title": "Chandigarh Food and Shopping",
   "days": 2,
   "season": "October to March",
   "cost": 4000,
   "itinerary": [
    "Sector 17 and Sector 22 markets.",
    "Elante Mall and the food streets."
   ],
   "note": ""
  },
  {
   "title": "Le Corbusier Architecture Tour",
   "days": 2,
   "season": "October to March",
   "cost": 4500,
   "itinerary": [
    "Capitol Complex and Open Hand Monument.",
    "Le Corbusier Centre and Pierre Jeanneret Museum."
   ],
   "note": ""
  }
 ],
 "Dadra and Nagar Haveli and Daman and Diu": [
  {
   "title": "Diu Island",
   "days": 3,
   "season": "October to March",
   "cost": 8000,
   "itinerary": [
    "Diu Fort and St Paul's Church.",
    "Nagoa Beach and Gangeshwar Temple.",
    "INS Khukri Memorial and departure."
   ],
   "note": ""
  },
  {
   "title": "Daman and Silvassa",
   "days": 3,
   "season": "October to March",
   "cost": 6500,
   "itinerary": [
    "Moti Daman Fort and Jampore Beach.",
    "Silvassa: Tribal Cultural Museum.",
    "Vanganga Lake Garden and Dudhni Lake."
   ],
   "note": ""
  },
  {
   "title": "Silvassa Nature Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 5000,
   "itinerary": [
    "Vanganga Lake Garden and Dudhni Lake.",
    "Tribal Museum and Hirvavan Garden."
   ],
   "note": ""
  },
  {
   "title": "Daman Beaches",
   "days": 2,
   "season": "October to March",
   "cost": 5500,
   "itinerary": [
    "Devka Beach and Jampore Beach.",
    "Moti Daman Fort and Mirasol Lake Garden."
   ],
   "note": ""
  }
 ],
 "Lakshadweep": [
  {
   "title": "Agatti and Bangaram",
   "days": 5,
   "season": "October to May",
   "cost": 30000,
   "itinerary": [
    "Fly from Kochi to Agatti.",
    "Lagoon snorkelling and glass-bottom boat.",
    "Bangaram island day trip.",
    "Kayaking and beach time.",
    "Return to Kochi."
   ],
   "note": "An entry permit is required for Lakshadweep."
  },
  {
   "title": "Kadmat Water Sports",
   "days": 4,
   "season": "October to May",
   "cost": 26000,
   "itinerary": [
    "Arrive at Kadmat.",
    "Scuba diving or snorkelling.",
    "Kayaking and sailing.",
    "Return."
   ],
   "note": "An entry permit is required for Lakshadweep."
  },
  {
   "title": "Kavaratti Island",
   "days": 4,
   "season": "October to May",
   "cost": 28000,
   "itinerary": [
    "Fly from Kochi to Agatti, then boat to Kavaratti.",
    "Marine Aquarium and Ujra Mosque.",
    "Lagoon snorkelling.",
    "Return."
   ],
   "note": "An entry permit is required for Lakshadweep."
  },
  {
   "title": "Minicoy Island",
   "days": 5,
   "season": "October to May",
   "cost": 32000,
   "itinerary": [
    "Travel to Minicoy by ship or flight.",
    "Minicoy Lighthouse.",
    "Thundi Beach and a local dance show.",
    "Snorkelling.",
    "Return."
   ],
   "note": "An entry permit is required for Lakshadweep."
  }
 ],
 "Manipur": [
  {
   "title": "Imphal and Loktak Lake",
   "days": 4,
   "season": "October to March",
   "cost": 10000,
   "itinerary": [
    "Imphal: Kangla Fort and Ima Keithel market.",
    "INA Memorial at Moirang.",
    "Loktak Lake and Sendra Island.",
    "Keibul Lamjao National Park and return."
   ],
   "note": ""
  },
  {
   "title": "Ukhrul and Shirui Hills",
   "days": 4,
   "season": "April to June",
   "cost": 8500,
   "itinerary": [
    "Imphal to Ukhrul.",
    "Khayang Peak.",
    "Shirui Hills (the Shirui lily blooms around May and June).",
    "Return to Imphal."
   ],
   "note": ""
  },
  {
   "title": "Imphal Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 6500,
   "itinerary": [
    "Kangla Fort and Ima Keithel.",
    "War Cemetery and Shree Govindajee Temple."
   ],
   "note": ""
  },
  {
   "title": "Loktak Lake Homestay",
   "days": 3,
   "season": "November to March",
   "cost": 9500,
   "itinerary": [
    "Arrive at Loktak Lake.",
    "Phumdi homestay and Sendra Island.",
    "Keibul Lamjao National Park and return."
   ],
   "note": ""
  }
 ],
 "Mizoram": [
  {
   "title": "Aizawl and Hills",
   "days": 4,
   "season": "October to March",
   "cost": 11000,
   "itinerary": [
    "Aizawl: Mizoram State Museum and Bara Bazar.",
    "Durtlang Hills.",
    "Reiek Heritage Village.",
    "Return."
   ],
   "note": "Inner Line Permit is needed."
  },
  {
   "title": "Champhai and Vantawng",
   "days": 3,
   "season": "November to March",
   "cost": 9500,
   "itinerary": [
    "Aizawl to Champhai.",
    "Rih Dil Lake and Murlen National Park.",
    "Vantawng Falls near Serchhip and return."
   ],
   "note": "Inner Line Permit is needed."
  },
  {
   "title": "Aizawl Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 6500,
   "itinerary": [
    "Mizoram State Museum and Bara Bazar.",
    "Durtlang Hills and Solomon's Temple."
   ],
   "note": "Inner Line Permit is needed."
  },
  {
   "title": "Phawngpui Blue Mountain",
   "days": 4,
   "season": "October to March",
   "cost": 10000,
   "itinerary": [
    "Aizawl to Saiha.",
    "Phawngpui National Park.",
    "Blue Mountain viewpoint.",
    "Return."
   ],
   "note": "Inner Line Permit is needed."
  }
 ],
 "Nagaland": [
  {
   "title": "Kohima and Hornbill Festival",
   "days": 5,
   "season": "December",
   "cost": 14000,
   "itinerary": [
    "Kohima: War Cemetery and State Museum.",
    "Kisama Heritage Village.",
    "Hornbill Festival (early December).",
    "Khonoma Green Village.",
    "Return."
   ],
   "note": "Inner Line Permit is needed. The Hornbill Festival is held in early December."
  },
  {
   "title": "Mon and Konyak Villages",
   "days": 4,
   "season": "October to May",
   "cost": 11000,
   "itinerary": [
    "Arrive in Mon.",
    "Shangnyu village.",
    "Longwa village.",
    "Return."
   ],
   "note": "Inner Line Permit is needed."
  },
  {
   "title": "Dzukou Valley Trek",
   "days": 3,
   "season": "June to September, November to March",
   "cost": 8500,
   "itinerary": [
    "Kohima to Viswema.",
    "Trek to Dzukou Valley.",
    "Camp in the valley and trek down."
   ],
   "note": "Inner Line Permit is needed."
  },
  {
   "title": "Kohima Weekend",
   "days": 2,
   "season": "October to April",
   "cost": 6500,
   "itinerary": [
    "War Cemetery and State Museum.",
    "Kisama Heritage Village and Khonoma."
   ],
   "note": "Inner Line Permit is needed."
  }
 ],
 "Puducherry": [
  {
   "title": "French Quarter",
   "days": 3,
   "season": "October to March",
   "cost": 8500,
   "itinerary": [
    "White Town and Promenade Beach.",
    "Sri Aurobindo Ashram and Auroville (Matrimandir).",
    "Paradise Beach and departure."
   ],
   "note": ""
  },
  {
   "title": "Auroville and Beaches",
   "days": 2,
   "season": "October to March",
   "cost": 6000,
   "itinerary": [
    "Serenity Beach and Auroville.",
    "Heritage walk, Basilica of the Sacred Heart of Jesus and departure."
   ],
   "note": ""
  },
  {
   "title": "Chidambaram and Puducherry",
   "days": 3,
   "season": "October to March",
   "cost": 8000,
   "itinerary": [
    "Puducherry: White Town and Promenade Beach.",
    "Auroville.",
    "Chidambaram Nataraja Temple and return."
   ],
   "note": ""
  },
  {
   "title": "Food and Cafe Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 5500,
   "itinerary": [
    "White Town cafes and French bakeries.",
    "Beach breakfast and the Sunday market."
   ],
   "note": ""
  }
 ],
 "Andaman and Nicobar Islands": [
  {
   "title": "Port Blair and Havelock",
   "days": 6,
   "season": "October to May",
   "cost": 28000,
   "itinerary": [
    "Port Blair: Cellular Jail and the light and sound show.",
    "Ross Island and North Bay.",
    "Ferry to Havelock. Radhanagar Beach.",
    "Elephant Beach (snorkelling).",
    "Neil Island: Bharatpur Beach.",
    "Return to Port Blair."
   ],
   "note": ""
  },
  {
   "title": "Neil Island and Baratang",
   "days": 5,
   "season": "November to April",
   "cost": 24000,
   "itinerary": [
    "Arrive in Port Blair.",
    "Baratang: limestone caves.",
    "Ferry to Neil Island. Natural Bridge.",
    "Scuba diving or snorkelling.",
    "Return."
   ],
   "note": ""
  },
  {
   "title": "Port Blair Weekend",
   "days": 3,
   "season": "October to May",
   "cost": 18000,
   "itinerary": [
    "Cellular Jail and Corbyn's Cove.",
    "Chidiya Tapu and Samudrika Naval Marine Museum.",
    "Departure."
   ],
   "note": ""
  },
  {
   "title": "Diglipur and Ross and Smith Islands",
   "days": 4,
   "season": "November to April",
   "cost": 22000,
   "itinerary": [
    "Port Blair to Diglipur.",
    "Ross and Smith Islands.",
    "Saddle Peak trek.",
    "Return."
   ],
   "note": "Roads and ferries may be affected by weather."
  }
 ],
 "Sikkim": [
  {
   "title": "Gangtok and Tsomgo Lake",
   "days": 5,
   "season": "March to May, October to December",
   "cost": 16000,
   "itinerary": [
    "Gangtok: MG Marg.",
    "Rumtek Monastery.",
    "Tsomgo Lake and Baba Mandir.",
    "Nathu La Pass (if open).",
    "Return."
   ],
   "note": "Tsomgo Lake and Nathu La need a permit. Nathu La is closed on Mondays and Tuesdays."
  },
  {
   "title": "North Sikkim Highlands",
   "days": 5,
   "season": "March to June",
   "cost": 18000,
   "itinerary": [
    "Gangtok to Lachung.",
    "Yumthang Valley.",
    "Lachung to Lachen.",
    "Gurudongmar Lake.",
    "Return."
   ],
   "note": "North Sikkim needs a permit."
  },
  {
   "title": "Pelling and Ravangla",
   "days": 4,
   "season": "March to June, October to December",
   "cost": 14000,
   "itinerary": [
    "Arrive in Pelling.",
    "Pemayangtse Monastery and Rabdentse Ruins.",
    "Skywalk and Kanchenjunga viewpoint.",
    "Ravangla: Buddha Park and return."
   ],
   "note": ""
  },
  {
   "title": "Gangtok Weekend",
   "days": 2,
   "season": "March to June, October to December",
   "cost": 8500,
   "itinerary": [
    "MG Marg and Ganesh Tok.",
    "Rumtek Monastery and Enchey Monastery."
   ],
   "note": ""
  }
 ],
 "Meghalaya": [
  {
   "title": "Shillong and Cherrapunji",
   "days": 4,
   "season": "October to May",
   "cost": 11500,
   "itinerary": [
    "Shillong: Elephant Falls and the Don Bosco Museum.",
    "Cherrapunji: Nohkalikai Falls and Mawsmai Cave.",
    "Double-decker living root bridge at Nongriat.",
    "Return."
   ],
   "note": ""
  },
  {
   "title": "Dawki and Mawlynnong",
   "days": 3,
   "season": "November to March",
   "cost": 9000,
   "itinerary": [
    "Arrive in Shillong.",
    "Dawki: boating on the Umngot River.",
    "Mawlynnong village and departure."
   ],
   "note": ""
  },
  {
   "title": "Shillong Weekend",
   "days": 2,
   "season": "October to May",
   "cost": 6500,
   "itinerary": [
    "Ward's Lake and Police Bazaar.",
    "Shillong Peak and Umiam Lake."
   ],
   "note": ""
  },
  {
   "title": "Jowai and Krang Suri",
   "days": 3,
   "season": "November to March",
   "cost": 8500,
   "itinerary": [
    "Shillong to Jowai.",
    "Krang Suri Falls.",
    "Thadlaskein Lake and return."
   ],
   "note": ""
  }
 ],
 "Gujarat": [
  {
   "title": "Kutch and the White Rann",
   "days": 4,
   "season": "November to February",
   "cost": 12000,
   "itinerary": [
    "Bhuj: Aina Mahal and Prag Mahal.",
    "Kala Dungar.",
    "White Rann of Kutch and the Rann Utsav tents.",
    "Return."
   ],
   "note": ""
  },
  {
   "title": "Somnath and Gir",
   "days": 4,
   "season": "December to March",
   "cost": 11500,
   "itinerary": [
    "Junagadh: Uperkot Fort.",
    "Somnath Temple.",
    "Gir National Park lion safari.",
    "Return."
   ],
   "note": "Gir is closed in monsoon, mid-June to mid-October."
  },
  {
   "title": "Statue of Unity and Vadodara",
   "days": 3,
   "season": "October to March",
   "cost": 8000,
   "itinerary": [
    "Vadodara: Laxmi Vilas Palace.",
    "Statue of Unity.",
    "Champaner-Pavagadh (UNESCO World Heritage)."
   ],
   "note": ""
  },
  {
   "title": "Ahmedabad Heritage",
   "days": 3,
   "season": "October to March",
   "cost": 7500,
   "itinerary": [
    "Sabarmati Ashram and Sidi Saiyyed Mosque.",
    "Adalaj Stepwell and Jama Masjid.",
    "Law Garden food walk."
   ],
   "note": ""
  }
 ],
 "Rajasthan": [
  {
   "title": "Jaipur Pink City",
   "days": 3,
   "season": "October to March",
   "cost": 9000,
   "itinerary": [
    "Amer Fort and Jal Mahal.",
    "City Palace, Hawa Mahal and Jantar Mantar.",
    "Nahargarh Fort sunset and Johari Bazaar."
   ],
   "note": ""
  },
  {
   "title": "Desert Circuit",
   "days": 6,
   "season": "October to March",
   "cost": 20000,
   "itinerary": [
    "Jodhpur: Mehrangarh Fort and Jaswant Thada.",
    "Drive to Jaisalmer. Gadisar Lake.",
    "Jaisalmer Fort and Patwon Ki Haveli.",
    "Sam Sand Dunes camel safari and night camp.",
    "Ranakpur Jain Temple and drive to Udaipur.",
    "Udaipur: City Palace and Lake Pichola."
   ],
   "note": ""
  },
  {
   "title": "Udaipur Lakes",
   "days": 3,
   "season": "October to March",
   "cost": 11000,
   "itinerary": [
    "City Palace and Lake Pichola boat ride.",
    "Saheliyon Ki Bari and Fateh Sagar.",
    "Kumbhalgarh Fort day trip."
   ],
   "note": ""
  },
  {
   "title": "Ranthambore Tiger Safari",
   "days": 3,
   "season": "October to June",
   "cost": 12000,
   "itinerary": [
    "Arrive at Ranthambore.",
    "Morning safari and Ranthambore Fort.",
    "Evening safari and return."
   ],
   "note": "The park is closed from July to September."
  }
 ],
 "Jammu and Kashmir": [
  {
   "title": "Srinagar Valley",
   "days": 5,
   "season": "April to October",
   "cost": 16000,
   "itinerary": [
    "Srinagar: Dal Lake shikara and houseboat.",
    "Mughal Gardens: Nishat and Shalimar.",
    "Gulmarg Gondola.",
    "Pahalgam: Betaab Valley.",
    "Sonamarg: Thajiwas Glacier. Return."
   ],
   "note": "Check current travel advisories before you book."
  },
  {
   "title": "Vaishno Devi Yatra",
   "days": 3,
   "season": "March to November",
   "cost": 8000,
   "itinerary": [
    "Jammu: Raghunath Temple and Bahu Fort.",
    "Katra to the Vaishno Devi shrine (about 12 km trek).",
    "Return to Katra and departure."
   ],
   "note": "Yatra registration is required."
  },
  {
   "title": "Pahalgam and Aru Valley",
   "days": 3,
   "season": "April to October",
   "cost": 11000,
   "itinerary": [
    "Srinagar to Pahalgam.",
    "Aru Valley and Chandanwari.",
    "Return."
   ],
   "note": "Check current travel advisories before you book."
  },
  {
   "title": "Gulmarg Winter Trip",
   "days": 4,
   "season": "December to February",
   "cost": 14000,
   "itinerary": [
    "Srinagar: Dal Lake.",
    "Gulmarg Gondola and skiing.",
    "Day at Gulmarg.",
    "Return."
   ],
   "note": "Check current travel advisories before you book."
  }
 ],
 "Tripura": [
  {
   "title": "Agartala and Neermahal",
   "days": 3,
   "season": "October to March",
   "cost": 8500,
   "itinerary": [
    "Agartala: Ujjayanta Palace.",
    "Neermahal on Rudrasagar Lake.",
    "Tripura Sundari Temple in Udaipur and return."
   ],
   "note": ""
  },
  {
   "title": "Unakoti and Jampui Hills",
   "days": 4,
   "season": "October to March",
   "cost": 9500,
   "itinerary": [
    "Arrive in Agartala.",
    "Sepahijala Wildlife Sanctuary.",
    "Unakoti rock carvings.",
    "Jampui Hills and return."
   ],
   "note": ""
  },
  {
   "title": "Agartala Weekend",
   "days": 2,
   "season": "October to March",
   "cost": 5500,
   "itinerary": [
    "Ujjayanta Palace and the State Museum.",
    "Heritage Park and Jagannath Temple."
   ],
   "note": ""
  },
  {
   "title": "Dumboor Lake and Matabari",
   "days": 3,
   "season": "October to March",
   "cost": 8000,
   "itinerary": [
    "Agartala to Matabari. Tripura Sundari Temple.",
    "Gumti Wildlife Sanctuary.",
    "Dumboor Lake boat ride and return."
   ],
   "note": ""
  }
 ]
};
