document.addEventListener("DOMContentLoaded",(function(){var e=document.querySelector("#filter-make"),t=document.querySelector("#filter-model"),c=document.querySelector("#type_of_vehicle"),n=document.querySelector("#trim_filter"),o=document.querySelector("#apply-filters-button");e.addEventListener("change",(function(){var c=["All"];fetch("/report/get_models",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({makeSelected:e.value})}).then((function(e){return e.json()})).then((function(e){c.push.apply(c,e.models),t.innerHTML="",c.forEach((function(e){var c=document.createElement("option");c.value=e,c.textContent=e,t.appendChild(c)})),o.click()})).catch((function(e){console.error("Error sending data to Flask:",e)}))})),t.addEventListener("change",(function(){o.click()})),c.addEventListener("change",(function(){o.click()})),n.addEventListener("change",(function(){o.click()})),document.querySelector("#views_options").addEventListener("change",(function(){o.click()}));var r=document.querySelector("#views-column-button"),i=(document.querySelector("#views-na"),document.querySelector("#views-asc")),u=document.querySelector("#views-desc");r.addEventListener("click",(function(){i.hasAttribute("selected")?(i.removeAttribute("selected"),u.setAttribute("selected","selected")):u.hasAttribute("selected")&&(u.removeAttribute("selected"),i.setAttribute("selected","selected")),o.click()}));var d=document.querySelector("#price-button"),l=document.querySelector("#price-inputs");d.addEventListener("click",(function(){l.classList.toggle("hidden")})),document.querySelector("#date_received").addEventListener("input",(function(){o.click()}));var a=document.querySelector("#download-button"),s=document.querySelector("#download");a.addEventListener("click",(function(){s.value="true",o.click()}));var v=document.querySelector("#exclude");document.querySelectorAll(".delete-from-report").forEach((function(e){e.addEventListener("click",(function(){if("None"===v.value)return v.value="".concat(e.getAttribute("data-target"),","),void o.click();v.value+="".concat(e.getAttribute("data-target"),","),o.click()}))}))}));