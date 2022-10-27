import React, { useEffect, useState } from "react";
import { useRouter } from "next/router";
import { useSelector } from "react-redux";
import AppLayout from "../../components/hocs/AppLayout";
import SelectBoard from "../../components/BoardPage/SelectBoard";

const AppPage = () => {
  const loading = useSelector((state) => state.auth.loading);
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

  const router = useRouter();

  useEffect(() => {
    if (typeof window !== undefined && !loading && !isAuthenticated) {
      router.push("/login");
    }
  }, []);

  return (
    <AppLayout title="Kanban App | Dashboard">
      <SelectBoard />
    </AppLayout>
  );
};

export default AppPage;
