if(!localStorage.getItem('count'))
{
    localStorage.setItem('count',0);
}
//let counter=0
        function count()
        {
            let counter=parseInt(localStorage.getItem('count'));
            counter+=1;
            document.querySelector("h1").innerHTML=counter;

            localStorage.setItem('count ',counter);
            if (counter %10 == 0)
            {
                alert(`counter reach ${counter}`)
            }

        }


        document.addEventListener('DOMContentLoaded',function(){
            //document.querySelector('button').onclick=count;
            document.querySelector("h1").innerHTML=localStorage.getItem('count');
            setInterval(count,1000);
        });
