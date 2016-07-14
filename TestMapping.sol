contract TestMapping {
	 mapping (uint => uint) public storedData;

	 function set(uint key, uint data){
	 	  storedData[key] =  data;
	 }
	 function get(uint key) constant returns(uint retVal){
	 return storedData[key];
	 }
}