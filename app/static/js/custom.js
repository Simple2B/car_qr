/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!***********************!*\
  !*** ./src/custom.ts ***!
  \***********************/
document.addEventListener('DOMContentLoaded', function () {
    var basic_plan = document.querySelector('#basic_plan_card');
    var advanced_plan = document.querySelector('#advanced_plan_card');
    var basicPlanButton = document.querySelector('#basic_radio');
    var advancedPlanButton = document.querySelector('#advanced_radio');
    var planChosen = document.querySelector('#plan_chosen');
    if (planChosen) {
        var planChosenData = planChosen.dataset.plan;
        if (planChosenData != 'Advanced Plan') {
            basic_plan.classList.add('indigo');
            basic_plan.classList.add('text-white');
            advanced_plan.classList.remove('indigo');
            advanced_plan.classList.remove('text-white');
            basicPlanButton.checked = true;
        }
        else {
            advanced_plan.classList.add('indigo');
            advanced_plan.classList.add('text-white');
            basic_plan.classList.remove('indigo');
            basic_plan.classList.remove('text-white');
            advancedPlanButton.checked = true;
        }
        basic_plan.addEventListener('click', function () {
            basic_plan.classList.add('indigo');
            basic_plan.classList.add('text-white');
            advanced_plan.classList.remove('indigo');
            advanced_plan.classList.remove('text-white');
            if (basicPlanButton.checked == true) {
                basicPlanButton.checked = false;
            }
            else {
                basicPlanButton.checked = true;
                basicPlanButton.style.display = 'none';
            }
        });
        advanced_plan.addEventListener('click', function () {
            advanced_plan.classList.add('indigo');
            advanced_plan.classList.add('text-white');
            basic_plan.classList.remove('indigo');
            basic_plan.classList.remove('text-white');
            if (advancedPlanButton.checked == true) {
                advancedPlanButton.checked = false;
            }
            else {
                advancedPlanButton.checked = true;
                advancedPlanButton.style.display = 'none';
            }
        });
    }
});
var cleanEmail = document.querySelector('.clean_email_input');
if (cleanEmail) {
    cleanEmail.addEventListener('input', function (e) {
        if (e.target.value) {
            var inputText = e.target.value.replace(/[^\w\d_.@-]/gi, '');
            e.target.value = inputText;
        }
    });
}
var cleanNameInputs = document.querySelectorAll('.clean_name_input');
if (cleanNameInputs) {
    cleanNameInputs.forEach(function (cleanNameInput) {
        cleanNameInput.addEventListener('input', function (e) {
            if (e.target.value) {
                var inputText = e.target.value.replace(/[^\w\d\s.-]/gi, '');
                e.target.value = inputText;
            }
        });
    });
}
var cleanNumberInputs = document.querySelectorAll('.clean_number_input');
cleanNumberInputs.forEach(function (cleanNumberInput) {
    cleanNumberInput.addEventListener('input', function (e) {
        if (e.target.value) {
            var inputText = e.target.value.replace(/[^\d]/gi, '');
            e.target.value = inputText;
        }
    });
});
var cleanPhone = document.querySelector('.clean_phone_input');
if (cleanPhone) {
    cleanPhone.addEventListener('input', function (e) {
        if (e.target.value) {
            var x = e.target.value
                .replace(/\D/g, '')
                .match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
            e.target.value =
                x[1] +
                    (x[2] ? "-".concat(x[2]) : '') +
                    (x[3] ? "-".concat(x[3]) : '') +
                    (x[4] ? "-".concat(x[4]) : '');
        }
    });
}
var pricingButton = document.querySelector('#pricing_button');
pricingButton.addEventListener('click', function (event) {
    event.preventDefault();
    document.querySelector('#pricing').scrollIntoView({
        behavior: 'smooth',
    });
});
var contactButton = document.querySelector('#contact_button');
contactButton.addEventListener('click', function (event) {
    event.preventDefault();
    document.querySelector('#contacts').scrollIntoView({
        behavior: 'smooth',
    });
});
var firstArrowButton = document.querySelector('#first_arrow');
firstArrowButton.addEventListener('click', function (event) {
    event.preventDefault();
    document.querySelector('#second_section').scrollIntoView({
        behavior: 'smooth',
    });
});
var secondArrowButtons = document.querySelectorAll('.second_arrow');
secondArrowButtons.forEach(function (secondArrowButton) {
    secondArrowButton.addEventListener('click', function (event) {
        event.preventDefault();
        document.querySelector('#fourth_section').scrollIntoView({
            behavior: 'smooth',
        });
    });
});
// Select the elements to reveal
var revealElements = document.querySelectorAll('.reveal-element');
// Create an Intersection Observer instance
var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
        if (entry.isIntersecting) {
            if (entry.target.classList.contains('qr-code')) {
                entry.target.classList.add('flipInY');
                entry.target.classList.add('animated');
                entry.target.classList.add('reveal'); // Add the "reveal" class to trigger the animation
            }
            else {
                entry.target.classList.add('reveal'); // Add the "reveal" class to trigger the animation
                observer.unobserve(entry.target); // Stop observing once revealed
            }
        }
    });
}, { threshold: 0.5 }); // Adjust the threshold as needed
// Start observing each reveal element
revealElements.forEach(function (element) {
    observer.observe(element);
});
var landing_mobile_menu_button = document.querySelector('#landing_mobile_menu_button');
var landing_mobile_menu = document.querySelector('#landing_mobile_menu');
var footer = document.querySelector('footer');
var sections = document.querySelectorAll('section');
if (landing_mobile_menu_button) {
    landing_mobile_menu_button.addEventListener('click', function () {
        landing_mobile_menu.classList.toggle('hidden');
        footer.classList.toggle('hidden');
        sections.forEach(function (section) {
            section.classList.toggle('hidden');
        });
    });
}
var mobile_pricing = document.querySelector('#mobile_pricing');
var mobile_contacts = document.querySelector('#mobile_contact');
console.log(mobile_contacts);
if (mobile_pricing) {
    mobile_pricing.addEventListener('click', function () {
        landing_mobile_menu.classList.toggle('hidden');
        footer.classList.toggle('hidden');
        sections.forEach(function (section) {
            section.classList.toggle('hidden');
        });
        document.querySelector('#pricing').scrollIntoView({
            behavior: 'smooth',
        });
    });
}
if (mobile_contacts) {
    console.log(mobile_contacts);
    mobile_contacts.addEventListener('click', function () {
        landing_mobile_menu.classList.toggle('hidden');
        footer.classList.toggle('hidden');
        sections.forEach(function (section) {
            section.classList.toggle('hidden');
        });
        document.querySelector('#contacts').scrollIntoView({
            behavior: 'smooth',
        });
    });
}

/******/ })()
;
//# sourceMappingURL=data:application/json;charset=utf-8;base64,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QUFDLFNBQVMsQ0FBQyxNQUFNLENBQUMsUUFBUSxDQUFDLENBQUM7UUFDbEMsUUFBUSxDQUFDLE9BQU8sQ0FBQyxpQkFBTztZQUN0QixPQUFPLENBQUMsU0FBUyxDQUFDLE1BQU0sQ0FBQyxRQUFRLENBQUMsQ0FBQztRQUNyQyxDQUFDLENBQUMsQ0FBQztRQUNILFFBQVEsQ0FBQyxhQUFhLENBQUMsVUFBVSxDQUFDLENBQUMsY0FBYyxDQUFDO1lBQ2hELFFBQVEsRUFBRSxRQUFRO1NBQ25CLENBQUMsQ0FBQztJQUNMLENBQUMsQ0FBQyxDQUFDO0NBQ0o7QUFFRCxJQUFJLGVBQWUsRUFBRTtJQUNuQixPQUFPLENBQUMsR0FBRyxDQUFDLGVBQWUsQ0FBQyxDQUFDO0lBQzdCLGVBQWUsQ0FBQyxnQkFBZ0IsQ0FBQyxPQUFPLEVBQUU7UUFDeEMsbUJBQW1CLENBQUMsU0FBUyxDQUFDLE1BQU0sQ0FBQyxRQUFRLENBQUMsQ0FBQztRQUMvQyxNQUFNLENBQUMsU0FBUyxDQUFDLE1BQU0sQ0FBQyxRQUFRLENBQUMsQ0FBQztRQUNsQyxRQUFRLENBQUMsT0FBTyxDQUFDLGlCQUFPO1lBQ3RCLE9BQU8sQ0FBQyxTQUFTLENBQUMsTUFBTSxDQUFDLFFBQVEsQ0FBQyxDQUFDO1FBQ3JDLENBQUMsQ0FBQyxDQUFDO1FBQ0gsUUFBUSxDQUFDLGFBQWEsQ0FBQyxXQUFXLENBQUMsQ0FBQyxjQUFjLENBQUM7WUFDakQsUUFBUSxFQUFFLFFBQVE7U0FDbkIsQ0FBQyxDQUFDO0lBQ0wsQ0FBQyxDQUFDLENBQUM7Q0FDSiIsInNvdXJjZXMiOlsid2VicGFjazovL3N0YXRpYy8uL3NyYy9jdXN0b20udHMiXSwic291cmNlc0NvbnRlbnQiOlsiZG9jdW1lbnQuYWRkRXZlbnRMaXN0ZW5lcignRE9NQ29udGVudExvYWRlZCcsIGZ1bmN0aW9uICgpIHtcbiAgY29uc3QgYmFzaWNfcGxhbjogRWxlbWVudCA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNiYXNpY19wbGFuX2NhcmQnKTtcbiAgY29uc3QgYWR2YW5jZWRfcGxhbjogRWxlbWVudCA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNhZHZhbmNlZF9wbGFuX2NhcmQnKTtcbiAgY29uc3QgYmFzaWNQbGFuQnV0dG9uOiBIVE1MSW5wdXRFbGVtZW50ID1cbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcjYmFzaWNfcmFkaW8nKTtcbiAgY29uc3QgYWR2YW5jZWRQbGFuQnV0dG9uOiBIVE1MSW5wdXRFbGVtZW50ID1cbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcjYWR2YW5jZWRfcmFkaW8nKTtcblxuICBjb25zdCBwbGFuQ2hvc2VuOiBIVE1MRGl2RWxlbWVudCA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNwbGFuX2Nob3NlbicpO1xuICBpZiAocGxhbkNob3Nlbikge1xuICAgIGNvbnN0IHBsYW5DaG9zZW5EYXRhID0gcGxhbkNob3Nlbi5kYXRhc2V0LnBsYW47XG5cbiAgICBpZiAocGxhbkNob3NlbkRhdGEgIT0gJ0FkdmFuY2VkIFBsYW4nKSB7XG4gICAgICBiYXNpY19wbGFuLmNsYXNzTGlzdC5hZGQoJ2luZGlnbycpO1xuICAgICAgYmFzaWNfcGxhbi5jbGFzc0xpc3QuYWRkKCd0ZXh0LXdoaXRlJyk7XG4gICAgICBhZHZhbmNlZF9wbGFuLmNsYXNzTGlzdC5yZW1vdmUoJ2luZGlnbycpO1xuICAgICAgYWR2YW5jZWRfcGxhbi5jbGFzc0xpc3QucmVtb3ZlKCd0ZXh0LXdoaXRlJyk7XG4gICAgICBiYXNpY1BsYW5CdXR0b24uY2hlY2tlZCA9IHRydWU7XG4gICAgfSBlbHNlIHtcbiAgICAgIGFkdmFuY2VkX3BsYW4uY2xhc3NMaXN0LmFkZCgnaW5kaWdvJyk7XG4gICAgICBhZHZhbmNlZF9wbGFuLmNsYXNzTGlzdC5hZGQoJ3RleHQtd2hpdGUnKTtcbiAgICAgIGJhc2ljX3BsYW4uY2xhc3NMaXN0LnJlbW92ZSgnaW5kaWdvJyk7XG4gICAgICBiYXNpY19wbGFuLmNsYXNzTGlzdC5yZW1vdmUoJ3RleHQtd2hpdGUnKTtcbiAgICAgIGFkdmFuY2VkUGxhbkJ1dHRvbi5jaGVja2VkID0gdHJ1ZTtcbiAgICB9XG5cbiAgICBiYXNpY19wbGFuLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4ge1xuICAgICAgYmFzaWNfcGxhbi5jbGFzc0xpc3QuYWRkKCdpbmRpZ28nKTtcbiAgICAgIGJhc2ljX3BsYW4uY2xhc3NMaXN0LmFkZCgndGV4dC13aGl0ZScpO1xuICAgICAgYWR2YW5jZWRfcGxhbi5jbGFzc0xpc3QucmVtb3ZlKCdpbmRpZ28nKTtcbiAgICAgIGFkdmFuY2VkX3BsYW4uY2xhc3NMaXN0LnJlbW92ZSgndGV4dC13aGl0ZScpO1xuXG4gICAgICBpZiAoYmFzaWNQbGFuQnV0dG9uLmNoZWNrZWQgPT0gdHJ1ZSkge1xuICAgICAgICBiYXNpY1BsYW5CdXR0b24uY2hlY2tlZCA9IGZhbHNlO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgYmFzaWNQbGFuQnV0dG9uLmNoZWNrZWQgPSB0cnVlO1xuICAgICAgICBiYXNpY1BsYW5CdXR0b24uc3R5bGUuZGlzcGxheSA9ICdub25lJztcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIGFkdmFuY2VkX3BsYW4uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoKSA9PiB7XG4gICAgICBhZHZhbmNlZF9wbGFuLmNsYXNzTGlzdC5hZGQoJ2luZGlnbycpO1xuICAgICAgYWR2YW5jZWRfcGxhbi5jbGFzc0xpc3QuYWRkKCd0ZXh0LXdoaXRlJyk7XG4gICAgICBiYXNpY19wbGFuLmNsYXNzTGlzdC5yZW1vdmUoJ2luZGlnbycpO1xuICAgICAgYmFzaWNfcGxhbi5jbGFzc0xpc3QucmVtb3ZlKCd0ZXh0LXdoaXRlJyk7XG5cbiAgICAgIGlmIChhZHZhbmNlZFBsYW5CdXR0b24uY2hlY2tlZCA9PSB0cnVlKSB7XG4gICAgICAgIGFkdmFuY2VkUGxhbkJ1dHRvbi5jaGVja2VkID0gZmFsc2U7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBhZHZhbmNlZFBsYW5CdXR0b24uY2hlY2tlZCA9IHRydWU7XG4gICAgICAgIGFkdmFuY2VkUGxhbkJ1dHRvbi5zdHlsZS5kaXNwbGF5ID0gJ25vbmUnO1xuICAgICAgfVxuICAgIH0pO1xuICB9XG59KTtcblxuY29uc3QgY2xlYW5FbWFpbDogSFRNTElucHV0RWxlbWVudCA9XG4gIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5jbGVhbl9lbWFpbF9pbnB1dCcpO1xuaWYgKGNsZWFuRW1haWwpIHtcbiAgY2xlYW5FbWFpbC5hZGRFdmVudExpc3RlbmVyKCdpbnB1dCcsIChlOiBhbnkpID0+IHtcbiAgICBpZiAoZS50YXJnZXQudmFsdWUpIHtcbiAgICAgIGNvbnN0IGlucHV0VGV4dCA9IGUudGFyZ2V0LnZhbHVlLnJlcGxhY2UoL1teXFx3XFxkXy5ALV0vZ2ksICcnKTtcbiAgICAgIGUudGFyZ2V0LnZhbHVlID0gaW5wdXRUZXh0O1xuICAgIH1cbiAgfSk7XG59XG5cbmNvbnN0IGNsZWFuTmFtZUlucHV0cyA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5jbGVhbl9uYW1lX2lucHV0Jyk7XG5pZiAoY2xlYW5OYW1lSW5wdXRzKSB7XG4gIGNsZWFuTmFtZUlucHV0cy5mb3JFYWNoKGNsZWFuTmFtZUlucHV0ID0+IHtcbiAgICBjbGVhbk5hbWVJbnB1dC5hZGRFdmVudExpc3RlbmVyKCdpbnB1dCcsIChlOiBhbnkpID0+IHtcbiAgICAgIGlmIChlLnRhcmdldC52YWx1ZSkge1xuICAgICAgICBjb25zdCBpbnB1dFRleHQgPSBlLnRhcmdldC52YWx1ZS5yZXBsYWNlKC9bXlxcd1xcZFxccy4tXS9naSwgJycpO1xuICAgICAgICBlLnRhcmdldC52YWx1ZSA9IGlucHV0VGV4dDtcbiAgICAgIH1cbiAgICB9KTtcbiAgfSk7XG59XG5cbmNvbnN0IGNsZWFuTnVtYmVySW5wdXRzOiBOb2RlTGlzdE9mPEhUTUxJbnB1dEVsZW1lbnQ+ID1cbiAgZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgnLmNsZWFuX251bWJlcl9pbnB1dCcpO1xuY2xlYW5OdW1iZXJJbnB1dHMuZm9yRWFjaChjbGVhbk51bWJlcklucHV0ID0+IHtcbiAgY2xlYW5OdW1iZXJJbnB1dC5hZGRFdmVudExpc3RlbmVyKCdpbnB1dCcsIChlOiBhbnkpID0+IHtcbiAgICBpZiAoZS50YXJnZXQudmFsdWUpIHtcbiAgICAgIGNvbnN0IGlucHV0VGV4dCA9IGUudGFyZ2V0LnZhbHVlLnJlcGxhY2UoL1teXFxkXS9naSwgJycpO1xuICAgICAgZS50YXJnZXQudmFsdWUgPSBpbnB1dFRleHQ7XG4gICAgfVxuICB9KTtcbn0pO1xuXG5jb25zdCBjbGVhblBob25lOiBIVE1MSW5wdXRFbGVtZW50ID1cbiAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLmNsZWFuX3Bob25lX2lucHV0Jyk7XG5pZiAoY2xlYW5QaG9uZSkge1xuICBjbGVhblBob25lLmFkZEV2ZW50TGlzdGVuZXIoJ2lucHV0JywgKGU6IGFueSkgPT4ge1xuICAgIGlmIChlLnRhcmdldC52YWx1ZSkge1xuICAgICAgY29uc3QgeCA9IGUudGFyZ2V0LnZhbHVlXG4gICAgICAgIC5yZXBsYWNlKC9cXEQvZywgJycpXG4gICAgICAgIC5tYXRjaCgvKFxcZHswLDN9KShcXGR7MCwzfSkoXFxkezAsNH0pLyk7XG4gICAgICBlLnRhcmdldC52YWx1ZSA9XG4gICAgICAgIHhbMV0gK1xuICAgICAgICAoeFsyXSA/IGAtJHt4WzJdfWAgOiAnJykgK1xuICAgICAgICAoeFszXSA/IGAtJHt4WzNdfWAgOiAnJykgK1xuICAgICAgICAoeFs0XSA/IGAtJHt4WzRdfWAgOiAnJyk7XG4gICAgfVxuICB9KTtcbn1cblxuY29uc3QgcHJpY2luZ0J1dHRvbjogRWxlbWVudCA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNwcmljaW5nX2J1dHRvbicpO1xucHJpY2luZ0J1dHRvbi5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIGV2ZW50ID0+IHtcbiAgZXZlbnQucHJldmVudERlZmF1bHQoKTtcbiAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcignI3ByaWNpbmcnKS5zY3JvbGxJbnRvVmlldyh7XG4gICAgYmVoYXZpb3I6ICdzbW9vdGgnLFxuICB9KTtcbn0pO1xuXG5jb25zdCBjb250YWN0QnV0dG9uOiBFbGVtZW50ID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignI2NvbnRhY3RfYnV0dG9uJyk7XG5jb250YWN0QnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgZXZlbnQgPT4ge1xuICBldmVudC5wcmV2ZW50RGVmYXVsdCgpO1xuICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcjY29udGFjdHMnKS5zY3JvbGxJbnRvVmlldyh7XG4gICAgYmVoYXZpb3I6ICdzbW9vdGgnLFxuICB9KTtcbn0pO1xuXG5jb25zdCBmaXJzdEFycm93QnV0dG9uOiBFbGVtZW50ID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignI2ZpcnN0X2Fycm93Jyk7XG5maXJzdEFycm93QnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgZXZlbnQgPT4ge1xuICBldmVudC5wcmV2ZW50RGVmYXVsdCgpO1xuICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcjc2Vjb25kX3NlY3Rpb24nKS5zY3JvbGxJbnRvVmlldyh7XG4gICAgYmVoYXZpb3I6ICdzbW9vdGgnLFxuICB9KTtcbn0pO1xuXG5jb25zdCBzZWNvbmRBcnJvd0J1dHRvbnMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcuc2Vjb25kX2Fycm93Jyk7XG5cbnNlY29uZEFycm93QnV0dG9ucy5mb3JFYWNoKHNlY29uZEFycm93QnV0dG9uID0+IHtcbiAgc2Vjb25kQXJyb3dCdXR0b24uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCBldmVudCA9PiB7XG4gICAgZXZlbnQucHJldmVudERlZmF1bHQoKTtcbiAgICBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcjZm91cnRoX3NlY3Rpb24nKS5zY3JvbGxJbnRvVmlldyh7XG4gICAgICBiZWhhdmlvcjogJ3Ntb290aCcsXG4gICAgfSk7XG4gIH0pO1xufSk7XG5cbi8vIFNlbGVjdCB0aGUgZWxlbWVudHMgdG8gcmV2ZWFsXG5jb25zdCByZXZlYWxFbGVtZW50cyA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5yZXZlYWwtZWxlbWVudCcpO1xuXG4vLyBDcmVhdGUgYW4gSW50ZXJzZWN0aW9uIE9ic2VydmVyIGluc3RhbmNlXG5jb25zdCBvYnNlcnZlciA9IG5ldyBJbnRlcnNlY3Rpb25PYnNlcnZlcihcbiAgZW50cmllcyA9PiB7XG4gICAgZW50cmllcy5mb3JFYWNoKGVudHJ5ID0+IHtcbiAgICAgIGlmIChlbnRyeS5pc0ludGVyc2VjdGluZykge1xuICAgICAgICBpZiAoZW50cnkudGFyZ2V0LmNsYXNzTGlzdC5jb250YWlucygncXItY29kZScpKSB7XG4gICAgICAgICAgZW50cnkudGFyZ2V0LmNsYXNzTGlzdC5hZGQoJ2ZsaXBJblknKTtcbiAgICAgICAgICBlbnRyeS50YXJnZXQuY2xhc3NMaXN0LmFkZCgnYW5pbWF0ZWQnKTtcbiAgICAgICAgICBlbnRyeS50YXJnZXQuY2xhc3NMaXN0LmFkZCgncmV2ZWFsJyk7IC8vIEFkZCB0aGUgXCJyZXZlYWxcIiBjbGFzcyB0byB0cmlnZ2VyIHRoZSBhbmltYXRpb25cbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICBlbnRyeS50YXJnZXQuY2xhc3NMaXN0LmFkZCgncmV2ZWFsJyk7IC8vIEFkZCB0aGUgXCJyZXZlYWxcIiBjbGFzcyB0byB0cmlnZ2VyIHRoZSBhbmltYXRpb25cbiAgICAgICAgICBvYnNlcnZlci51bm9ic2VydmUoZW50cnkudGFyZ2V0KTsgLy8gU3RvcCBvYnNlcnZpbmcgb25jZSByZXZlYWxlZFxuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG4gIH0sXG4gIHt0aHJlc2hvbGQ6IDAuNX0sXG4pOyAvLyBBZGp1c3QgdGhlIHRocmVzaG9sZCBhcyBuZWVkZWRcblxuLy8gU3RhcnQgb2JzZXJ2aW5nIGVhY2ggcmV2ZWFsIGVsZW1lbnRcbnJldmVhbEVsZW1lbnRzLmZvckVhY2goZWxlbWVudCA9PiB7XG4gIG9ic2VydmVyLm9ic2VydmUoZWxlbWVudCk7XG59KTtcblxuY29uc3QgbGFuZGluZ19tb2JpbGVfbWVudV9idXR0b246IEhUTUxCdXR0b25FbGVtZW50ID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcbiAgJyNsYW5kaW5nX21vYmlsZV9tZW51X2J1dHRvbicsXG4pO1xuY29uc3QgbGFuZGluZ19tb2JpbGVfbWVudTogSFRNTERpdkVsZW1lbnQgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFxuICAnI2xhbmRpbmdfbW9iaWxlX21lbnUnLFxuKTtcbmNvbnN0IGZvb3RlcjogSFRNTEVsZW1lbnQgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCdmb290ZXInKTtcbmNvbnN0IHNlY3Rpb25zOiBOb2RlTGlzdE9mPEhUTUxFbGVtZW50PiA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJ3NlY3Rpb24nKTtcbmlmIChsYW5kaW5nX21vYmlsZV9tZW51X2J1dHRvbikge1xuICBsYW5kaW5nX21vYmlsZV9tZW51X2J1dHRvbi5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsICgpID0+IHtcbiAgICBsYW5kaW5nX21vYmlsZV9tZW51LmNsYXNzTGlzdC50b2dnbGUoJ2hpZGRlbicpO1xuICAgIGZvb3Rlci5jbGFzc0xpc3QudG9nZ2xlKCdoaWRkZW4nKTtcbiAgICBzZWN0aW9ucy5mb3JFYWNoKHNlY3Rpb24gPT4ge1xuICAgICAgc2VjdGlvbi5jbGFzc0xpc3QudG9nZ2xlKCdoaWRkZW4nKTtcbiAgICB9KTtcbiAgfSk7XG59XG5cbmNvbnN0IG1vYmlsZV9wcmljaW5nOiBIVE1MRGl2RWxlbWVudCA9XG4gIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNtb2JpbGVfcHJpY2luZycpO1xuY29uc3QgbW9iaWxlX2NvbnRhY3RzOiBIVE1MRGl2RWxlbWVudCA9XG4gIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNtb2JpbGVfY29udGFjdCcpO1xuY29uc29sZS5sb2cobW9iaWxlX2NvbnRhY3RzKTtcblxuaWYgKG1vYmlsZV9wcmljaW5nKSB7XG4gIG1vYmlsZV9wcmljaW5nLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4ge1xuICAgIGxhbmRpbmdfbW9iaWxlX21lbnUuY2xhc3NMaXN0LnRvZ2dsZSgnaGlkZGVuJyk7XG4gICAgZm9vdGVyLmNsYXNzTGlzdC50b2dnbGUoJ2hpZGRlbicpO1xuICAgIHNlY3Rpb25zLmZvckVhY2goc2VjdGlvbiA9PiB7XG4gICAgICBzZWN0aW9uLmNsYXNzTGlzdC50b2dnbGUoJ2hpZGRlbicpO1xuICAgIH0pO1xuICAgIGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNwcmljaW5nJykuc2Nyb2xsSW50b1ZpZXcoe1xuICAgICAgYmVoYXZpb3I6ICdzbW9vdGgnLFxuICAgIH0pO1xuICB9KTtcbn1cblxuaWYgKG1vYmlsZV9jb250YWN0cykge1xuICBjb25zb2xlLmxvZyhtb2JpbGVfY29udGFjdHMpO1xuICBtb2JpbGVfY29udGFjdHMuYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoKSA9PiB7XG4gICAgbGFuZGluZ19tb2JpbGVfbWVudS5jbGFzc0xpc3QudG9nZ2xlKCdoaWRkZW4nKTtcbiAgICBmb290ZXIuY2xhc3NMaXN0LnRvZ2dsZSgnaGlkZGVuJyk7XG4gICAgc2VjdGlvbnMuZm9yRWFjaChzZWN0aW9uID0+IHtcbiAgICAgIHNlY3Rpb24uY2xhc3NMaXN0LnRvZ2dsZSgnaGlkZGVuJyk7XG4gICAgfSk7XG4gICAgZG9jdW1lbnQucXVlcnlTZWxlY3RvcignI2NvbnRhY3RzJykuc2Nyb2xsSW50b1ZpZXcoe1xuICAgICAgYmVoYXZpb3I6ICdzbW9vdGgnLFxuICAgIH0pO1xuICB9KTtcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==