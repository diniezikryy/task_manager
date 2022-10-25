import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { useQuery } from "@tanstack/react-query";
import { API_URL } from "../../config/index";
import Layout from "../../hocs/Layout";
import axios from "axios";
import { useRouter } from "next/router";

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
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const loading = useSelector((state) => state.auth.loading);
  const router = useRouter();

  async function fetchUserData() {
    const { data } = await axios.get("/api/kanbanapp/getUserData", {
      method: "GET",
      headers: {
        Accept: "application/json",
      },
    });
    return data;
  }

  const { data, error, isError, isLoading } = useQuery(["user"], () =>
    fetchUserData()
  );

  if (isError) {
    return <div>Error! {error.message}</div>;
  }

  if (typeof window !== "undefined" && !loading && !isAuthenticated)
    router.push("/login");

  return (
    <div>
      <Layout title="Kanban App | User Page">
        {isLoading ? <div>Loading...</div> : <div>{data.user.first_name}</div>}
      </Layout>
    </div>
  );
};

export default UserPage;
