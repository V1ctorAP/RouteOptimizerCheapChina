using System;
using RouteOptimizer.Core.Repositories;

namespace RouteOptimizer.Core.Services
{
    public class PullRequestService
    {
        private readonly PullRequestRepository _repository;

        public PullRequestService(PullRequestRepository repository)
        {
            _repository = repository ?? throw new ArgumentNullException(nameof(repository));
        }

        public PullRequest ChangeTargetBranch(string pullRequestId, string newTargetBranch)
        {
            if (string.IsNullOrWhiteSpace(pullRequestId))
            {
                throw new ArgumentException("Pull request ID cannot be null or empty", nameof(pullRequestId));
            }

            if (string.IsNullOrWhiteSpace(newTargetBranch))
            {
                throw new ArgumentException("New target branch cannot be null or empty", nameof(newTargetBranch));
            }

            var pullRequest = _repository.GetPullRequestById(pullRequestId);
            if (pullRequest == null)
            {
                throw new ArgumentException("Pull request not found", nameof(pullRequestId));
            }

            pullRequest.TargetBranch = newTargetBranch;
            _repository.UpdatePullRequest(pullRequest);

            return pullRequest;
        }
    }
}
