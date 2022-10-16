import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { useQuery } from "@tanstack/react-query";
import { API_URL } from "../../config/index";
import Layout from "../../hocs/Layout";
import axios from "axios";

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
  const access_token = useSelector((state) => state.auth.access_token);
  console.log(access_token);

  /* const fetchUserData = async () => {
    const { data } = await axios.get(
      `${API_URL}/api/account/users/${userData.id}`,
      {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      }
    );
    return data;
  };

  const { data, error, isError, isLoading } = useQuery(
    ["userDetails"],
    fetchUserData
  );

  if (isLoading) return "Loading...";

  if (isError) return <div>Error! {error.message}</div>;

  console.log(data); */

  return (
    <div>
      <Layout title="Kanban App | User Page">
        <p>User page of user {data.first_name}</p>
      </Layout>
    </div>
  );
};

export default UserPage;
