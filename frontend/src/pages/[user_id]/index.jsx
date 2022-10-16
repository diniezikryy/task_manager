import React, { useEffect, useState } from "react";
import { API_URL } from "../../config/index";
import Layout from "../../hocs/Layout";

export const getStaticPaths = async (req, res) => {
  const apiRes = await fetch(`${API_URL}/api/account/users`, {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
  });
  const data = await apiRes.json();

  const paths = data.users.map((user) => {
    return {
      params: { user_id: user.id.toString() },
    };
  });

  return {
    paths: paths,
    fallback: false,
  };
};

export const getStaticProps = async (context) => {
  const id = context.params.user_id;
  const apiRes = await fetch(`${API_URL}/api/account/users/${id}`, {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
  });
  const data = await apiRes.json();

  return {
    props: { userData: data.user },
  };
};

const UserPage = ({ userData }) => {
  return (
    <div>
      <Layout title="Kanban App | User Page">
        <p>User page of user {userData.username}</p>
      </Layout>
    </div>
  );
};

export default UserPage;
