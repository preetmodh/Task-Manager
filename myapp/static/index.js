document.addEventListener('DOMContentLoaded', function() {


  document.querySelector('#all').addEventListener('click',load_all);
  document.querySelector('#archived').addEventListener('click',load_c);
  document.querySelector('#new').addEventListener('click', new_list);
  load_all();
});

const newLocal = '#co-view';
function new_list() {
  document.querySelector('#new-view').style.display = 'block';
  document.querySelector(newLocal).style.display = 'none';
  document.querySelector('#all-view').style.display = 'none';
}

function load_all() {
  document.querySelector('#all-view').style.display = 'block';
  document.querySelector(newLocal).style.display = 'none';
  document.querySelector('#new-view').style.display = 'none';
}
function load_c() {
  document.querySelector(newLocal).style.display = 'block';
  document.querySelector('#new-view').style.display = 'none';
  document.querySelector('#all-view').style.display = 'none';
}