var building1 = { 'Gym': 0, 'School': 1, 'Store': 0 }
var building2 = { 'Gym': 1, 'School': 0, 'Store': 0 }
var building3 = { 'Gym': 1, 'School': 1, 'Store': 0 }
var building4 = { 'Gym': 0, 'School': 1, 'Store': 0 }
var building5 = { 'Gym': 0, 'School': 1, 'Store': 1 }
var list1 = [building1, building2, building3, building4, building5]

var gym = [], school = [], store = [];
counter=0
for (j = 0; j < list1.length; j++) {
    if (list1[j].Gym) {
        gym.push(j)
    }
    if (list1[j].School) {
        school.push(j)
    }
    if (list1[j].Store) {
        store.push(j)
    }
    
}
console.log(gym,school,store)
var n=list1.length
for(i=0;i<n;i++){

}