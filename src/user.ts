import {Modal} from 'flowbite';
import type {ModalOptions, ModalInterface} from 'flowbite';

interface IUser {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
}

const $modalElement: HTMLElement = document.querySelector('#editUserModal');
const $modalResendInviteElement: HTMLElement =
  document.querySelector('#resendInviteModal');
const $addUserModalElement: HTMLElement =
  document.querySelector('#add-user-modal');

const modalOptions: ModalOptions = {
  placement: 'bottom-right',
  backdrop: 'dynamic',
  backdropClasses:
    'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40',
  closable: true,
  onHide: () => {},
  onShow: () => {},
  onToggle: () => {},
};

const modal: ModalInterface = new Modal($modalElement, modalOptions);
const resendInviteModal: ModalInterface = new Modal(
  $modalResendInviteElement,
  modalOptions,
);
const addModal: ModalInterface = new Modal($addUserModalElement, modalOptions);

const $buttonElements = document.querySelectorAll('.user-edit-button');
$buttonElements.forEach(e =>
  e.addEventListener('click', () => {
    editUser(JSON.parse(e.getAttribute('data-target')));
  }),
);

const resendInviteButtons = document.querySelectorAll('.resend-invite-button');
resendInviteButtons.forEach(e =>
  e.addEventListener('click', () => {
    const user = JSON.parse(e.getAttribute('data-target'));
    resendInvite(user);
  }),
);

// closing add edit modal
const $buttonClose = document.querySelector('#modalCloseButton');
if ($buttonClose) {
  $buttonClose.addEventListener('click', () => {
    modal.hide();
  });
}

const resendInviteButtonClose = document.querySelector(
  '#resendInviteModalCloseButton',
);
if (resendInviteButtonClose) {
  resendInviteButtonClose.addEventListener('click', () => {
    resendInviteModal.hide();
  });
}

const searchInput: HTMLInputElement = document.querySelector(
  '#table-search-users',
);
const searchInputButton = document.querySelector('#table-search-user-button');

let searchTimeoutId: NodeJS.Timeout | null = null;

function performSearch() {
  const url = new URL(window.location.href);
  url.searchParams.set('q', searchInput.value);
  window.location.href = url.href;
}

function debounceSearch() {
  if (searchTimeoutId) {
    clearTimeout(searchTimeoutId);
  }
  searchTimeoutId = setTimeout(() => {
    performSearch();
  }, 2000);
}

if (searchInputButton && searchInput) {
  searchInputButton.addEventListener('click', () => {
    performSearch();
  });

  searchInput.addEventListener('keyup', event => {
    if (event.key === 'Enter') {
      performSearch();
    }
  });

  searchInput.addEventListener('input', debounceSearch);
}

const deleteButtons = document.querySelectorAll('.delete-user-btn');

deleteButtons.forEach(e => {
  e.addEventListener('click', async () => {
    if (confirm('Are sure?')) {
      let id = e.getAttribute('data-user-id');
      const response = await fetch(`/user/delete/${id}`, {
        method: 'DELETE',
      });
      if (response.status == 200) {
        location.reload();
      }
    }
  });
});

function editUser(user: IUser) {
  let input: HTMLInputElement = document.querySelector('#user-edit-firstname');
  input.value = user.first_name;
  input = document.querySelector('#user-edit-lastname');
  input.value = user.last_name;
  input = document.querySelector('#user-edit-id');
  input.value = user.id.toString();
  input = document.querySelector('#user-edit-email');
  input.value = user.email;
  input = document.querySelector('#user-edit-password');
  input.value = '*******';
  input = document.querySelector('#user-edit-password_confirmation');
  input.value = '*******';
  input = document.querySelector('#user-edit-next_url');
  input.value = window.location.href;
  modal.show();
}

function resendInvite(user?: IUser) {
  let input: HTMLInputElement;

  if (user) {
    input = document.querySelector('#resend-invite-id');
    input.value = user.id.toString();
    input = document.querySelector('#resend-invite-email');
    input.value = user.email;
  }
  input = document.querySelector('#resend-invite-next_url');
  input.value = window.location.href;
  resendInviteModal.show();
}
