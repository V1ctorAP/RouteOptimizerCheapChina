using System;
using RouteOptimizer.API.Controllers;

namespace RouteOptimizer.Web.UI
{
    public class PullRequestUI
    {
        private readonly PullRequestController _controller;

        public PullRequestUI(PullRequestController controller)
        {
            _controller = controller ?? throw new ArgumentNullException(nameof(controller));
        }

        public void ChangeTargetBranch(string pullRequestId, string newTargetBranch)
        {
            if (string.IsNullOrWhiteSpace(pullRequestId))
            {
                Console.WriteLine("Pull request ID cannot be null or empty");
                return;
            }

            if (string.IsNullOrWhiteSpace(newTargetBranch))
            {
                Console.WriteLine("New target branch cannot be null or empty");
                return;
            }

            try
            {
                var response = _controller.ChangeTargetBranch(pullRequestId, newTargetBranch);
                if (response.IsSuccessStatusCode)
                {
                    Console.WriteLine("Target branch changed successfully.");
                }
                else
                {
                    Console.WriteLine($"Failed to change target branch. Status code: {response.StatusCode}");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
