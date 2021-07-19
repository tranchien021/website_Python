var updateBtns = document.getElementsByClassName('update-cart')

    for(var i = 0; i < updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
        var courseId = this.dataset.courses
        var action = this.dataset.action
        console.log('courseId: ', courseId, 'action: ', action)

        console.log('USER: ', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in.')
        }else{
             updateUserOrder(courseId, action)
                }
            })
        }


        function updateUserOrder(courseId, action){
            console.log('User is authenticated. Sending data...')

            var url = '/update_item/'

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type':'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body: JSON.stringify({'courseId': courseId, 'action': action})
            })

            .then((response) => {
                return response.json()
            })

            .then((data) => {
                console.log('data: ', data)

            })
        }



