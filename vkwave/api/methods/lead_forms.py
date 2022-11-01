from vkwave.types.responses import *

from ._category import Category
from ._utils import get_params


class LeadForms(Category):
    async def create(
        self,
        group_id: int,
        name: str,
        title: str,
        description: str,
        questions: str,
        policy_link_url: str,
        photo: typing.Optional[str],
        confirmation: typing.Optional[str],
        site_link_url: typing.Optional[str],
        active: typing.Optional[bool],
        once_per_user: typing.Optional[bool],
        pixel_code: typing.Optional[str],
        notify_admins: typing.Optional[typing.List[int]],
        notify_emails: typing.Optional[typing.List[str]],
        return_raw_response: bool = False,
    ) -> typing.Union[dict, LeadFormsCreateResponse]:
        """leadForms.create method

        :param group_id:
        :param name:
        :param title:
        :param description:
        :param questions:
        :param policy_link_url:
        :param photo:
        :param confirmation:
        :param site_link_url:
        :param active:
        :param once_per_user:
        :param pixel_code:
        :param notify_admins:
        :param notify_emails:
        :param return_raw_response: - return result at dict
        """

        params = get_params(locals())
        raw_result = await self.api_request("create", params)
        if return_raw_response:
            return raw_result

        result = LeadFormsCreateResponse(**raw_result)
        return result

    async def delete(
        self, group_id: int, form_id: int, return_raw_response: bool = False
    ) -> typing.Union[dict, LeadFormsDeleteResponse]:
        """leadForms.delete method

        :param group_id:
        :param form_id:
        :param return_raw_response: - return result at dict
        """

        params = get_params(locals())
        raw_result = await self.api_request("delete", params)
        if return_raw_response:
            return raw_result

        result = LeadFormsDeleteResponse(**raw_result)
        return result

    async def get(
        self, group_id: int, form_id: int, return_raw_response: bool = False
    ) -> typing.Union[dict, LeadFormsForm]:
        """leadForms.get method

        :param group_id:
        :param form_id:
        :param return_raw_response: - return result at dict
        """

        params = get_params(locals())
        raw_result = await self.api_request("get", params)
        if return_raw_response:
            return raw_result

        result = LeadFormsForm(**raw_result)
        return result

    async def get_leads(
        self,
        group_id: int,
        form_id: int,
        limit: typing.Optional[int],
        next_page_token: typing.Optional[str],
        return_raw_response: bool = False,
    ) -> typing.Union[dict, LeadFormsGetLeadsResponse]:
        """leadForms.getLeads method

        :param group_id:
        :param form_id:
        :param limit:
        :param next_page_token:
        :param return_raw_response: - return result at dict
        """

        params = get_params(locals())
        raw_result = await self.api_request("getLeads", params)
        if return_raw_response:
            return raw_result

        result = LeadFormsGetLeadsResponse(**raw_result)
        return result

    async def get_upload_url(
        self, return_raw_response: bool = False
    ) -> typing.Union[dict, LeadFormsUploadUrlResponse]:
        """leadForms.getUploadURL method

        :param return_raw_response: - return result at dict
        """

        params = get_params(locals())
        raw_result = await self.api_request("getUploadURL", params)
        if return_raw_response:
            return raw_result

        result = LeadFormsUploadUrlResponse(**raw_result)
        return result

    async def list(
        self, group_id: int, return_raw_response: bool = False
    ) -> typing.Union[dict, LeadFormsListResponse]:
        """leadForms.list method

        :param group_id:
        :param return_raw_response: - return result at dict
        """

        params = get_params(locals())
        raw_result = await self.api_request("list", params)
        if return_raw_response:
            return raw_result

        result = LeadFormsListResponse(**raw_result)
        return result

    async def update(
        self,
        group_id: int,
        form_id: int,
        name: str,
        title: str,
        description: str,
        questions: str,
        policy_link_url: str,
        photo: typing.Optional[str],
        confirmation: typing.Optional[str],
        site_link_url: typing.Optional[str],
        active: typing.Optional[bool],
        once_per_user: typing.Optional[bool],
        pixel_code: typing.Optional[str],
        notify_admins: typing.Optional[typing.List[int]],
        notify_emails: typing.Optional[typing.List[str]],
        return_raw_response: bool = False,
    ) -> typing.Union[dict, LeadFormsCreateResponse]:
        """leadForms.update method

        :param group_id:
        :param form_id:
        :param name:
        :param title:
        :param description:
        :param questions:
        :param policy_link_url:
        :param photo:
        :param confirmation:
        :param site_link_url:
        :param active:
        :param once_per_user:
        :param pixel_code:
        :param notify_admins:
        :param notify_emails:
        :param return_raw_response: - return result at dict
        """

        params = get_params(locals())
        raw_result = await self.api_request("update", params)
        if return_raw_response:
            return raw_result

        result = LeadFormsCreateResponse(**raw_result)
        return result
